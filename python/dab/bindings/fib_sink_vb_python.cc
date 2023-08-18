/*
 * Copyright 2023 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 *
 */

/***********************************************************************************/
/* This file is automatically generated using bindtool and can be manually edited  */
/* The following lines can be configured to regenerate this file during cmake      */
/* If manual edits are made, the following tags should be modified accordingly.    */
/* BINDTOOL_GEN_AUTOMATIC(0)                                                       */
/* BINDTOOL_USE_PYGCCXML(0)                                                        */
/* BINDTOOL_HEADER_FILE(fib_sink_vb.h)                                        */
/* BINDTOOL_HEADER_FILE_HASH(c2ff642b968832c6b124608fa4b87c57)                     */
/***********************************************************************************/

#include <pybind11/complex.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

#include <gnuradio/dab/fib_sink_vb.h>
// pydoc.h is automatically generated in the build directory
#include <fib_sink_vb_pydoc.h>

void bind_fib_sink_vb(py::module& m)
{

    using fib_sink_vb = ::gr::dab::fib_sink_vb;


    py::class_<fib_sink_vb,
               gr::sync_block,
               gr::block,
               gr::basic_block,
               std::shared_ptr<fib_sink_vb>>(m, "fib_sink_vb", D(fib_sink_vb))

        .def(py::init(&fib_sink_vb::make), D(fib_sink_vb, make))


        .def("get_ensemble_info",
             &fib_sink_vb::get_ensemble_info,
             D(fib_sink_vb, get_ensemble_info))


        .def("get_service_info",
             &fib_sink_vb::get_service_info,
             D(fib_sink_vb, get_service_info))


        .def("get_service_labels",
             &fib_sink_vb::get_service_labels,
             D(fib_sink_vb, get_service_labels))


        .def("get_subch_info",
             &fib_sink_vb::get_subch_info,
             D(fib_sink_vb, get_subch_info))


        .def("get_programme_type",
             &fib_sink_vb::get_programme_type,
             D(fib_sink_vb, get_programme_type))


        .def("get_crc_passed",
             &fib_sink_vb::get_crc_passed,
             D(fib_sink_vb, get_crc_passed))


        .def("set_print_channel_info",
             &fib_sink_vb::set_print_channel_info,
             py::arg("val"),
             D(fib_sink_vb, set_print_channel_info))

        ;
}
