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
/* BINDTOOL_HEADER_FILE(unpuncture_ff.h)                                        */
/* BINDTOOL_HEADER_FILE_HASH(95cc0fe163de0a0722b6f550df6b7d33)                     */
/***********************************************************************************/

#include <pybind11/complex.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

#include <gnuradio/dab/unpuncture_ff.h>
// pydoc.h is automatically generated in the build directory
#include <unpuncture_ff_pydoc.h>

void bind_unpuncture_ff(py::module& m)
{

    using unpuncture_ff = ::gr::dab::unpuncture_ff;


    py::class_<unpuncture_ff, gr::block, gr::basic_block, std::shared_ptr<unpuncture_ff>>(
        m, "unpuncture_ff", D(unpuncture_ff))

        .def(py::init(&unpuncture_ff::make),
             py::arg("puncturing_vector"),
             py::arg("fillval") = 0,
             D(unpuncture_ff, make))


        ;
}
