[![License: CC BY-NC 4.0](https://img.shields.io/badge/License-CC%20BY--NC%204.0-lightgrey.svg)](https://creativecommons.org/licenses/by-nc/4.0/)

# Computing in Civil and Environmental Engineering

by Xiaofeng Liu, Ph.D., P.E.
Associate Professor

Department of Civil and Environmental Engineering  
Institute of Computational and Data Sciences  
Penn State University  
223B Sackett Building, University Park, PA 16802

Web: http://water.engr.psu.edu/liu/

# See static render on [nbviewer](https://nbviewer.jupyter.org/github/psu-efd/Computing-in-CEE/blob/master/index.ipynb)

GitHub does not support certain features in the Jupyter Notebook. You can view a static render on [nbviewer](https://nbviewer.jupyter.org/github/psu-efd/Computing-in-CEE/blob/master/index.ipynb).

# Why another book?

There are many many excellent books on the topic computational methods for engineers and scientists, as well as programming. However, through my teaching and research, I increasingly feel that there is a lack of discipline-specific textbook for civil and environmental engineers. Many of the books I used for my study and teaching are very general. They are geared toward a much broader audience, which is good. However, a consequence of this is that the content (description of each numerical method, examples, and exercise problems) may not be so relevant to civil and environmental engineers. This book is specifically designed to fill this hole. 

This work is far from complete. As of now, it is a collection of lecture notes in the form of Jupyter Notebooks using Python. These lecture notes are for the **Computing in Civil and Environmental Engineering** course that the author offers at Penn State. It will evolve as time goes by and may not reach completion before several batches of students go through this course.

Although the title of the book sounds like it is *ONLY* for civil and environmental engineers, it is envisioned that students and practioners from other disciplines, such as agricultural and biological engineering, architectural engineering, earth and mineral sciences, and geological sciences,  can find this work useful. 

# Overview and outline

This work is still evolving. As time goes by, more content and CEE-relevant examples will be added. The following is the outline and example list:
- Chapter 1: Basics
	- Text: 
		- Introduction to Jupyter Notebook
		- Introduction to Python
		- Installation of Python and libraries
		- Difference between Python v2 and v3
	- Examples:
		- Manning's equation for discharge calculation
		- Calculation of $\pi$ with Python
- Chapter 2: Root finding
	- Text: 
		- Root finding methods: bracketting methods (bisection method), open methods (Newton method and Secant method)
		- Python libraries for root finding
	- Examples:
		- Green-Ampt infiltration
		- Manning's equation for normal depth calculation
		- Beam deflection
		- Friction factor using the Colebrook-White formula
		- Particle settling in fluid
		- A step in open channel flow
- Chapter 3: Interpolation and curve fitting
	- Text:
		- Introduction
		- Least-square regression: linear regression, linearizable nonlinear regression, polynomial regression, and nonlinear regression
		- Interpolation
		- Python libraries for curve fitting
	- Examples:
		- Fluid rheological data fitting
		- Saturation growth rate
		- Surface area vs storage volume for a reservior
		- Flow velocity profile in open channel flows
		- Weir discharge coefficient
- Chapter 4: Linear system of equations
	- Text:
		- Introduction and background
		- Graphcial method
		- Direct solution methods: Determinant and Cramer's rule, Gauss elimination method, Gauss-Jordan method, LU decomposition method
		- Iterative solution methods: Jacobi method, Gauss-Seidel method, SOR method
		- Extra: marix vector operations in Python
	- Examples:
		- 2D truss
		- Steady state chemical reactor
		- Material mixing
- Chapter 5: Numerical integration
	- Text:
		- Introduction
		- Newton-Cotes methods: trapezoidal rule, Simpson's rule, double and multiple integrals
		- Gauss quadrature
		- Python libraries for numerical integration
	- Examples:
		- Arc length
		- Center of mass
		- Convolution integral
		- Discharge across a section
		- Fouries series coefficients
		- Hydrostatic force and moment on plane surface
		- Probability
- Chapter 6: Numerical differentiation
	- Text:
		- Introduction
		- Derivations of differential formulas: first-order, second-order, accuracy of numerical derivatives, some practical issues
		- Python libraries for numerical differentiation
	- Examples:
		- Heat conduction along a rod
		- Gradient calculation
- Chapter 7: Ordinary differential equations
	- Text:
		- Introduction and background
		- Initial value problems
		- Boundary value problems
		- Python libraries for ODEs
	- Examples:
		- Streeter-Phelps model for water quality
		- Backwater curve in open channels
		- Unsteady batch reactor
		- Mass-spring-damper system
		- Prey-predator model
		- Beam deflection
		- laminar boundary layer
		- Convective cooling
- Chapter 8: Partial differential equations
	- Text:
	- Examples:
		- Unsteady diffusion 
		- Laplace equation
		- Terzaghi 1D consolidation
		- Unsteady advection-diffusion
		- Waves
- Chapter 9: Optimaizations
	- Text: 
	- Examples:
		- Best hydraulic section in open channels
		- Transportation cost
		- Optimizing a 2D truss
- Chapter 10: Statistics

# How to contribute?

A project like this will definitely benefit from the community. Contributions in the following categories are welcome:
- Report of bugs and errors in the text and code
- CEE-relevant examples (either just an idea or full implementation): my background in water resources engineering may skew the examples more toward what we call the "wet" side of CEE. Thus, examples from the "dry" side are especially welcome. 
- Special topic suggestions: any topic not covered in the text but of relevance to the CEE profession. 

If you want to contribute, either create a pull request or simply send an email to: <xzl123@psu.edu>. 

# Acknowledgements

This work is partically supported by the Penn State CEE Harry West Teaching Award. 

# License

<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />This work is
<a href="https://raw.githubusercontent.com/psu-efd/Computing-in-CEE/master/LICENSE">licensed</a> under a <a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">Creative Commons Attribution-NonCommercial 4.0 International License</a>.

In essence, this work can be downloaded, used and re-distributed for non-commercial
purposes. You are free to share and adapt under the terms of attribution and noncommercial. 


# Author

Dr. Xiaofeng Liu (see [web](http://water.engr.psu.edu/liu/),
[twitter](https://twitter.com/Xiaofeng_Liu19)) is an associate professor in the Department of Civil and Environmental Engineering at the Pennsylvania State University. With background in civil engineering and applied mathematics, his main research interest is computational hydraulics and environmental flows. 
