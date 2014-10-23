=====
EzGal
=====

Websites
--------

* Main website:  http://www.baryons.org/ezgal/index.php

* Online Documentation:  http://www.baryons.org/ezgal/manual/

* ADS Entry:  http://adsabs.harvard.edu/abs/2012PASP..124..606M

* ASCL Entry:  http://ascl.net/1208.021


Description
-----------

EzGal is a tool that takes models of how the SED of a stellar population evolves with time and projects it through filters to calculate magnitude evolution and mass-to-light ratios as a function of redshift. For those familiar with the Bruzual and Charlot (2003) model set, this performs the same function as the program cm_evolution which is distributed with their models. EzGal can read in Bruzual and Charlot binary ised files as well as plain text files, allowing it to work with any model set. You can use it is a strictly command line utility to output text files for later use, or you can call it from python as a module to generate models on the fly. It can store the seds and evolution models in fits files for quick retrieval later. A convenient way to use it is to generate evolution models on a grid of formation redshifts for many filters, store all the calculated models in a single fits file, and then just use that fits file (in conjunction with EzGal) to quickly fetch redshift evolution models for all your gridded formation redshifts and filters. All this takes just a few lines of code.


Developers
----------

* Conor L. Mancone 

* Anthony H. Gonzalez


Citing EzGal
-------------

If using EzGal in a research paper, please cite the `EzGal paper <http://adsabs.harvard.edu/abs/2012PASP..124..606M>`_ published in PASP. We have included BibTeX entries for both the paper and the Astrophysics Source Code Library entry in the file `ezgal_refs.bib <https://github.com/dpgettings/ezgal/blob/master/ezgal_refs.bib>`_.

Additionally, as explained `here <http://www.baryons.org/ezgal/download.php#citing>`_, the magnitude evolution calcualations provided by EzGal are only possible because someone else has gone through effort of generating stellar evolution models. By using EzGal you are making use of multiple data products: EzGal itself, as well as whatever model sets you choose to use. Therefore it is important that you cite the paper which describes the model sets you are using. Here are the appropriate references:

========================   ===================================================================================================================
Model                      Reference
========================   ===================================================================================================================
PÉGASE.2                   `Fioc and Rocca-Volmerange 1997 (A&A, 326, 950) <http://adsabs.harvard.edu/abs/1997A%26A...326..950F>`_           
Bruzual and Charlot 2003   `Bruzual and Charlot 2003 (MNRAS, 344, 1000) <http://adsabs.harvard.edu/abs/2003MNRAS.344.1000B>`_                
Charlot and Bruzual 2007   Currently unpublished.  Please reference as an updated BC03 model.                                                
Maraston 2005              `Maraston et al. 2005 (MNRAS, 362, 799) <http://adsabs.harvard.edu/abs/2005MNRAS.362..799M>`_                     
BaSTI                      `Percival et al. 2009 (ApJ, 690, 472) <http://adsabs.harvard.edu/abs/2009ApJ...690..427P>`_                       
Conroy 2009                `Conroy, Gunn, and White 2009 (ApJ, 699, 486C) <http://adsabs.harvard.edu/abs/2009ApJ...699..486C>`_ 
                           and `Conroy and Gunn 2010 (ApJ, 712, 833C) <http://adsabs.harvard.edu/abs/2010ApJ...712..833C>`_  (Please cite both)  
========================   ===================================================================================================================

