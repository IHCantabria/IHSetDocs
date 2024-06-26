# Model formulation

## Overview

In the documentation, there are multiple proposals for shoreline models, such as static and dynamic equilibrium planform and profile models, as well as 3D, multiline, one-line evolution models, conceptual models or models tending to equilibrium, and hybrid models. The present project focuses on proposals for static and dynamic equilibrium and conceptual models for diagnostic studies, as well as one-line and hybrid models for detailed studies, which are computationally efficient, for medium, long, and very long-term projections. The following is a brief description of the models available in the above typologies, highlighting the proposals developed by the IGC Group:

### Models of static and dynamic beach equilibrium conditions

Several authors have been interested in proposing empirical formulations, which attempt to reproduce the static equilibrium conditions of both the beach profile planform. Regarding the profile, there are proposals for one section (e.g. Dean 1991), two sections (e.g. Bernabeu 1999), or even three sections (e.g. Requejo et al., 2008).

On the other hand, in terms of beach planform, there are numerous proposals considering expressions such as the logarithmic spiral (e.g. Silvester 1960), parabolic (e.g. Hsu and Evans 1989; González and Medina 2001; Elshinnawy et al., 2022), or hyperbolic tangent functions (e.g. Moreno and Kraus 1999). Despite the advantages and simplicity of the analytical formulations indicated above, these are not applicable in study sites with irregularities or obstacles in the bathymetry (reefs, rocky slabs,...). In these cases, the proposal presented by Gainza et al. (2018) is applicable.

#### [Static equilibrium (Beach Profile)](equilibrium_profile.md#static-equilibrium-beach-profile)
- [IHSetDean (Dean, 1991)](equilibrium_profile.md#ihsetdean-dean-1991)
- [IHSetBernabeu (Bernabeu et al., 2003)](equilibrium_profile.md#ihsetbernabeu-bernabeu-et-al-2003)

#### [Static equilibrium (Beach Planform)](equilibrium_planform.md#static-equilibrium-beach-planform)
- [IHSetGonzalez (Hsu and Evans, 1989; Gonzalez and Medina, 2001)](equilibrium_planform.md#ihsetgonzalez-hsu-and-evans-1989-gonzalez-and-medina-2001)

### Models of shoreline evolution tending to equilibrium

These models are conceptually based on the equilibrium between destructive and constructive forces acting on a beach. They allow the user to obtain the position of the shoreline at a given time, either due to the action of storms, seasonal changes, or changes caused by interannual effects. The approach of these models can be categorized according to the direction of sediment transport; either longitudinal or transverse. In the literature, several models have been proposed that only consider the transverse displacement of the coastline (e.g., Yates et al., 2009; Jara et al., 2015; Jaramillo et al. 2020).

Alternatively, there are few proposals that infer longshore processes. Among them, there are simplified models that reproduce changes in shoreline orientation which are mainly applicable to embedded beaches (e.g. Turki et al., 2013 and Jaramillo et al., 2021a). (As an integration of both processes, we have the IH-MOOSE model, proposed by Jaramillo et al., (2021b), which integrates cross-shore component, rotation, and parabolic plan shape expression, being a model tending to equilibrium applicable to embedded beaches.) 
The IH-MOOSE model incorporates processes described by Jaramillo et al. (2021b), including the cross-shore component, rotation, and parabolic planform expressions. These features aim to achieve equilibrium and are particularly relevant for embedded beaches.

#### [EBSEM - Cross-shore](ebsem_cross.md#equilibrium-based-shoreline-evolution-models-ebsem---cross-shore)
- [IHSetMillerDean (Miller and Dean, 2004)](ebsem_cross.md#ihsetmillerdean-miller-and-dean-2004)
- [IHSetYates (Yates et al., 2009)](ebsem_cross.md#ihsetyates-yates-et-al-2009)
- [IHSetShorefor (Davidson et al., 2013)](ebsem_cross.md#ihsetshorefor-davidson-et-al-2013)
- [IHSetJaramillo (Jaramillo et al., 2020)](ebsem_cross.md#ihsetjaramillo-jaramillo-et-al-2020)
- [IHSetLim (Lim et al., 2020)](ebsem_cross.md#ihsetlim-lim-et-al-2020)

#### [EBSEM - Longshore](ebsem_long.md#equilibrium-based-shoreline-evolution-models-ebsem---longshore)
- [IHSetTurki (Turki et al., 2013)](ebsem_long.md#ihsetturki-turki-et-al-2013)
- [IHSetJaramillo21a (Jaramillo et al., 2021a)](ebsem_long.md#ihsetjaramillo21a-jaramillo-et-al-2021a)


### One-line models.

One-line models are most commonly used to estimate long-term mean changes due to longitudinal sediment transport. These models use the sediment conservation formula considering turbulent flow and empirical longitudinal transport relationships, without addressing cross-shore transport. They assume that the profile maintains a constant shape that shifts seaward or landward during simulations, which means that they cannot be applied for the analysis of short-term changes in which transverse transport across the beach profile is significant. Within this typology, it is worth highlighting the CHRONOS model developed by the IGC Group of IHCantabria. This is a one-line model that simulates medium- to long-term changes (years), including wave propagation with the Ref-Dif OLUCA and Refract models, then updating the bathymetry for propagation and its evolution while preserving the sediment balance throughout the process.


#### [One-line models](one_line.md#one-line-models)
- [GENESIS (Hanson and Kraus, 1989)](one_line.md#genesis-hanson-and-kraus-1989)
- [CHRONOS (XXXX, XXXX)](one_line.md#chronos-xxxx-xxxx)

### Hybrid models.

Hybrid models consist of shoreline evolution models that combine transverse and longitudinal transport processes which are applicable on scales from days to decades. They are models of reduced complexity, with a reasonable computational cost, that assume a series of simplifying assumptions following the needs of the study. Examples of such models are the pioneering CosMos-COAST (Vitousek et al., 2017), IH-LANS (Alvarez-Cuesta et al., 2021), and IH-MOOSE (Jaramillo et al., 2021b). These hybrid models adopt several simplifying assumptions that allow coastline change calculations, considering both processes efficiently. Their major limitation, however, is that they do not preserve the sedimentary balance.

#### [Hybrid models](hybrid_model.md#hybrid-models)
- [IHSetIH-MOOSE (Jaramillo et al., 2021b)](hybrid_model.md#ihsetih-moose-jaramillo-et-al-2021b)


## Contents

```{toctree}
:maxdepth: 2

equilibrium_profile.md
equilibrium_planform.md
ebsem_cross.md
ebsem_long.md
hybrid_model.md
one_line.md