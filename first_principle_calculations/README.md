# NaMO<sub>2</sub>F<sub>2</sub> (M = Nb<sup>5+</sup>, Ta<sup>5+</sup>) Geometry Optimization and NMR Parameters Calculations

**Author:** Ouail Zakary  
**ORCID:** [0000-0002-7793-3306](https://orcid.org/0000-0002-7793-3306)  
**E-mail:** [Ouail.Zakary@oulu.fi](mailto:Ouail.Zakary@oulu.fi)  
**Website:** [Ouail_Zakary.html](https://cc.oulu.fi/~nmrwww/members/Ouail_Zakary.html)

This repository contains datasets from DFT calculations performed to optimize the local structures of NaMO<sub>2</sub>F<sub>2</sub> (M = Nb<sup>5+</sup>, Ta<sup>5+</sup>) and to compute their NMR parameters.

## Overview of the Data

The dataset includes both **inputs** (located in the folder: `INPUT_files`) and **outputs** (located in the folders: `OUTPUT_files`) for the following calculations:

1. **NMR Parameter Calculations for the Experimental Structure (ES):**  
   Based on X-ray powder diffraction patterns refined at room temperature using the Rietveld refinement method for NaNbO<sub>2</sub>F<sub>2</sub> and NaTaO<sub>2</sub>F<sub>2</sub>.  
   **Folder:** `./NaNbO2F2/ES_NMR` and `./NaTaO2F2/ES_NMR`

2. **Atomic Position Optimization (APO) of ES:**  
   **Folder:** `./NaNbO2F2/APO` and `./NaTaO2F2/APO`

3. **NMR Parameters Calculations of APO:**  
   **Folder:** `./NaNbO2F2/APO_NMR` and `./NaTaO2F2/APO_NMR`

4. **Full Optimization (FO) of ES:**  
   **Folder:** `./NaNbO2F2/FO` and `./NaTaO2F2/FO`

5. **NMR Parameters Calculations of FO:**  
   **Folder:** `./NaNbO2F2/FO_NMR` and `./NaTaO2F2/FO_NMR`

The `.slurm` files (named `<name>_jv_oz.slurm`, where `name` corresponds to each calculation) and the `.log` files (named `<name>_vasp_run.log`) can be found in their respective folders.

## Methods

### Geometry Optimization (APO and FO) using `VASP`

All first-principles calculations were performed using the **VASP** code (version 6.2.1). The **density functional theory (DFT)** approach used a wave function expanded on a plane-wave basis set, with a **550 eV** kinetic energy cut-off and a **(4 × 6 × 4)** shifted Monkhorst-Pack k-point mesh. The **Perdew–Burke–Ernzerhof (GGA-PBE)** functional was employed to obtain the ground state electronic structure. The interactions between core and valence electrons were treated using the **projector augmented wave (PAW)** method, incorporating core configurations for O, F, Na, Nb, and Ta.

Atomic positions were relaxed until forces converged to less than **0.1 meV/Å**, and total energy convergence was set to below **10<sup>–8</sup> eV**.

### NMR Parameters Calculations (ES_NMR, APO_NMR, and FO_NMR)

The **PAW** and **gauge including projector augmented wave (GIPAW)** methods were used to compute quadrupolar coupling NMR parameters (C<sub>Q</sub>, η<sub>Q</sub>) and magnetic shielding values (σ<sub>iso</sub>, σ<sub>CSA</sub>, η<sub>CSA</sub>). All parameters were set the same as those in the DFT relaxation process.

### Tensor Convention and Magnetic Shielding to Chemical Shift Conversion

Magnetic shielding tensors and experimental chemical shift parameters follow the **Haeberlen convention**. Definitions include:

- **Isotropic magnetic shielding (σ<sub>iso</sub>):** σ<sub>iso</sub> = (σ<sub>xx</sub> + σ<sub>yy</sub> + σ<sub>zz</sub>)/3  
- **Anisotropy of magnetic shielding (σ<sub>CSA</sub>):** σ<sub>CSA</sub> = σ<sub>zz</sub> – σ<sub>iso</sub>  
- **Asymmetry parameter (η<sub>CSA</sub>):** η<sub>CSA</sub> = (σ<sub>yy</sub> – σ<sub>xx</sub>)/σ<sub>CSA</sub>

In this study, NMR chemical shift values (δ<sub>iso</sub>) for **<sup>23</sup>Na** and **<sup>93</sup>Nb** were obtained from established linear regressions. For **<sup>19</sup>F**, new linear regressions from NaF and NaNbO<sub>2</sub>F<sub>2</sub> or NaTaO<sub>2</sub>F<sub>2</sub> were used.

## Directory Structure

The following directories contain the datasets:

- **NaNbO<sub>2</sub>F<sub>2</sub> Datasets:**
  - [APO INPUT files](./NaNbO2F2/APO/INPUT_files)
  - [APO OUTPUT files](./NaNbO2F2/APO/OUTPUT_files)
  - [APO_NMR INPUT files](./NaNbO2F2/APO_NMR/INPUT_files)
  - [APO_NMR OUTPUT files](./NaNbO2F2/APO_NMR/OUTPUT_files)
  - [ES_NMR INPUT files](./NaNbO2F2/ES_NMR/INPUT_files)
  - [ES_NMR OUTPUT files](./NaNbO2F2/ES_NMR/OUTPUT_files)
  - [FO INPUT files](./NaNbO2F2/FO/INPUT_files)
  - [FO OUTPUT files](./NaNbO2F2/FO/OUTPUT_files)
  - [FO_NMR INPUT files](./NaNbO2F2/FO_NMR/INPUT_files)
  - [FO_NMR OUTPUT files](./NaNbO2F2/FO_NMR/OUTPUT_files)

- **NaTaO<sub>2</sub>F<sub>2</sub> Datasets:**
  - [APO INPUT files](./NaTaO2F2/APO/INPUT_files)
  - [APO OUTPUT files](./NaTaO2F2/APO/OUTPUT_files)
  - [APO_NMR INPUT files](./NaTaO2F2/APO_NMR/INPUT_files)
  - [APO_NMR OUTPUT files](./NaTaO2F2/APO_NMR/OUTPUT_files)
  - [ES_NMR INPUT files](./NaTaO2F2/ES_NMR/INPUT_files)
  - [ES_NMR OUTPUT files](./NaTaO2F2/ES_NMR/OUTPUT_files)
  - [FO INPUT files](./NaTaO2F2/FO/INPUT_files)
  - [FO OUTPUT files](./NaTaO2F2/FO/OUTPUT_files)
  - [FO_NMR INPUT files](./NaTaO2F2/FO_NMR/INPUT_files)
  - [FO_NMR OUTPUT files](./NaTaO2F2/FO_NMR/OUTPUT_files)

For further details, please refer to the respective folders or contact the author via the provided email.