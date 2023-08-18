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
/* BINDTOOL_HEADER_FILE(magnitude_equalizer_vcc.h) */
/* BINDTOOL_HEADER_FILE_HASH(cfe7a7475ff46297429a29ae801374d1)                     */
/***********************************************************************************/

#include <pybind11/complex.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

#include <gnuradio/dab/magnitude_equalizer_vcc.h>
// pydoc.h is automatically generated in the build directory
#include <magnitude_equalizer_vcc_pydoc.h>

void bind_magnitude_equalizer_vcc(py::module& m)
{

    using magnitude_equalizer_vcc = ::gr::dab::magnitude_equalizer_vcc;


    py::class_<magnitude_equalizer_vcc,
               gr::sync_block,
               gr::block,
               gr::basic_block,
               std::shared_ptr<magnitude_equalizer_vcc>>(
        m, "magnitude_equalizer_vcc", D(magnitude_equalizer_vcc))

        .def(py::init(&magnitude_equalizer_vcc::make),
             py::arg("vlen"),
             py::arg("num_symbols"),
             D(magnitude_equalizer_vcc, make))


        ;
}