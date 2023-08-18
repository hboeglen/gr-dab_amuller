/* -*- c++ -*- */
/*
 * Copyright 2004 Free Software Foundation, Inc.
 * 
 * This file is part of GNU Radio
 * 
 * GNU Radio is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * GNU Radio is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with GNU Radio; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

/*
 * config.h is generated by configure.  It contains the results
 * of probing for features, options etc.  It should be the first
 * file included in your .cc file.
 */
#ifdef HAVE_CONFIG_H
#include "config.h"
#endif

#include <gnuradio/io_signature.h>
#include "ofdm_sampler_impl.h"

namespace gr {
  namespace dab {

ofdm_sampler::sptr
ofdm_sampler::make(unsigned int fft_length, unsigned int cp_length, unsigned int symbols_per_frame,unsigned int gap)
{
  return gnuradio::get_initial_sptr
    (new ofdm_sampler_impl(fft_length, cp_length, symbols_per_frame, gap));
}

ofdm_sampler_impl::ofdm_sampler_impl(unsigned int fft_length, unsigned int cp_length, unsigned int symbols_per_frame,unsigned int gap)
  : gr::block("ofdm_sampler",
             gr::io_signature::make (1, 1, sizeof(gr_complex)),
             gr::io_signature::make (1, 1, sizeof(gr_complex)*fft_length)),
  d_state(STATE_NS), d_pos(0), d_fft_length(fft_length), d_cp_length(cp_length), d_symbols_per_frame(symbols_per_frame), d_sym_nr(0), d_gap(gap), d_gap_left(0)
{
  assert(gap<=cp_length);
  set_relative_rate(1/float(fft_length+cp_length));
  set_tag_propagation_policy(TPP_DONT);
}

void 
ofdm_sampler_impl::forecast (int noutput_items, gr_vector_int &ninput_items_required)
{
  int in_req  = d_fft_length+d_cp_length-d_gap;
  // int in_req  = noutput_items * d_fft_length;
  unsigned ninputs = ninput_items_required.size ();
  for (unsigned i = 0; i < ninputs; i++)
    ninput_items_required[i] = in_req;
  // printf("dab_ofdm_sampler forecast: noutput_items: %d in_req: %d\n", noutput_items, in_req);
}


int
ofdm_sampler_impl::general_work (int noutput_items,
                   gr_vector_int &ninput_items,
                   gr_vector_const_void_star &input_items,
                   gr_vector_void_star &output_items)
{
  /* partially adapted from gr_ofdm_sampler.cc */
  const gr_complex *iptr = (const gr_complex *) input_items[0];
  
  gr_complex *optr = (gr_complex *) output_items[0];


  std::vector<int> tag_positions;
  int next_tag_position = -1;
  int next_tag_position_index = -1;

  // Get all stream tags with key "dab_sync", and make a vector of the positions.
  // "next_tag_position" contains the position within "iptr where the next "dab_sync" stream tag is found
  std::vector<tag_t> tags;
  get_tags_in_range(tags, 0, nitems_read(0), nitems_read(0) + ninput_items[0], pmt::mp("dab_sync"));
  for(int i=0;i<(int)tags.size();i++) {
      int current;
      current = tags[i].offset - nitems_read(0);
      tag_positions.push_back(current);
      next_tag_position_index = 0;
  }
  if(next_tag_position_index >= 0) {
      next_tag_position = tag_positions[next_tag_position_index];
  }

  unsigned int n_in = ninput_items[0];
  unsigned int index = 0;
  unsigned int out = 0;

  switch (d_state) {
    case(STATE_NS):
      {
      d_pos = 0;
      d_sym_nr = 0;
      d_gap_left = 0;
      bool trigger_now = false;
      while (index<n_in) {

        if ((unsigned int)next_tag_position == index) { /* trigger */
          next_tag_position_index++;
          if (next_tag_position_index == (int)tag_positions.size()) {
            next_tag_position_index = -1;
            next_tag_position = -1;
          }
          else {
            next_tag_position = tag_positions[next_tag_position_index];
          }
          // Action when stream tags is found:
          trigger_now = true;
          break;
          //
        }

        index++;
      }
      if (trigger_now)
        d_state = STATE_CP;
      else
        break;
      }
    case(STATE_CP):
      while (d_gap_left > 0 && index<n_in) { /* is there a gap left from the previous symbol? */
        index++;
        d_gap_left--;
      }
      while (index<n_in && d_pos < d_cp_length-d_gap) {
        index++;
        d_pos++;
      }
      if (d_pos == d_cp_length-d_gap)
        d_state = STATE_SYM;
      else
        break;
    case(STATE_SYM):
      if (index + d_fft_length <= n_in) {
        memcpy(&optr[out], &iptr[index], d_fft_length*sizeof(gr_complex));
        d_sym_nr++;
        index += d_fft_length;
        d_pos = 0;
        /* first symbol in frame? */
        if (d_sym_nr==1) // A stream tag called "first" is added for the first symbol in frame:
          add_item_tag(0, nitems_written(0) + out, pmt::intern("first"), pmt::intern(""), pmt::intern("ofdm_sampler"));
        out++;
        /* last symbol in frame? */
        if (d_sym_nr == d_symbols_per_frame) {
          d_state = STATE_NS;
        } else {
          d_state = STATE_CP;
          d_gap_left = d_gap;
        }
      }
      break;
  }
  consume_each(index);
  return out;
}

}

}
