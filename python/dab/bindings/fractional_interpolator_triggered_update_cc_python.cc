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
/* BINDTOOL_HEADER_FILE(fractional_interpolator_triggered_update_cc.h) */
/* BINDTOOL_HEADER_FILE_HASH(a01e5751923e38d937f1e6401075a610)                     */
/***********************************************************************************/

#include <pybind11/complex.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

#include <gnuradio/dab/fractional_interpolator_triggered_update_cc.h>
// pydoc.h is automatically generated in the build directory
#include <fractional_interpolator_triggered_update_cc_pydoc.h>

void bind_fractional_interpolator_triggered_update_cc(py::module& m)
{

    using fractional_interpolator_triggered_update_cc =
        ::gr::dab::fractional_interpolator_triggered_update_cc;


    py::class_<fractional_interpolator_triggered_update_cc,
               gr::block,
               gr::basic_block,
               std::shared_ptr<fractional_interpolator_triggered_update_cc>>(
        m,
        "fractional_interpolator_triggered_update_cc",
        D(fractional_interpolator_triggered_update_cc))

        .def(py::init(&fractional_interpolator_triggered_update_cc::make),
             py::arg("phase_shift"),
             py::arg("interp_ratio"),
             D(fractional_interpolator_triggered_update_cc, make))


        .def("set_interp_ratio",
             &fractional_interpolator_triggered_update_cc::set_interp_ratio,
             py::arg("interp_ratio"),
             D(fractional_interpolator_triggered_update_cc, set_interp_ratio))

        ;
}
