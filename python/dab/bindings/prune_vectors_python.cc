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
/* BINDTOOL_HEADER_FILE(prune_vectors.h)                                        */
/* BINDTOOL_HEADER_FILE_HASH(b24d3d75276234c02fa308503d5052c4)                     */
/***********************************************************************************/

#include <pybind11/complex.h>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

#include <gnuradio/dab/prune_vectors.h>
// pydoc.h is automatically generated in the build directory
#include <prune_vectors_pydoc.h>

void bind_prune_vectors(py::module& m)
{

    using prune_vectors = ::gr::dab::prune_vectors;


    py::class_<prune_vectors,
               gr::sync_block,
               gr::block,
               gr::basic_block,
               std::shared_ptr<prune_vectors>>(m, "prune_vectors", D(prune_vectors))

        .def(py::init(&prune_vectors::make),
             py::arg("itemsize"),
             py::arg("length"),
             py::arg("prune_start"),
             py::arg("prune_end"),
             D(prune_vectors, make))


        ;
}
