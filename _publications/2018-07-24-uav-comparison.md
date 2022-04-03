---
title: "Comparison of pre-and self-calibrated camera calibration models for UAS-derived nadir imagery for a SfM application"
authors: <b>David Griffiths</b>, Helene Burningham
collection: publications
permalink: /publication/camera-calibration-uas
excerpt: 'Linear topologies can be challenging terrains for SfM pipelines. A key source of error is caused by intrinsic camera distortions. We demonstrate through effective camera pre-calibration, distortions can be significantly reduced.'
date: 2018-07-24
venue: 'Progress in Physical Geography: Earth and Environment'
paperurl: 'https://journals.sagepub.com/doi/abs/10.1177/0309133318788964'
teaser: 'sfm_comparison.png'
---

![](/images/publications/uas-comparison.jpeg)

# Abstract

Structure from Motion (SfM) is a tool being increasingly utilised in geosciences for high-resolution three-dimensional mapping of landscapes. However, a number of authors have demonstrated that broad-scale systematic deformations, in the form of ‘doming’ and ‘bowling’, can occur when applied to linear (low-amplitude, feature-limited) topographies. In such contexts, a more rigorous lens calibration and ground control point acquisition process is required, which means that application of SfM to environments such as tidal flats or desert plains can be challenging. Uncertainties in elevation models generated through SfM were investigated here in the context of the low elevation, micro-topographic environment of saltmarsh. Eight digital surface models (DSMs) were generated for a saltmarsh site in the Deben Estuary (Suffolk, UK) using imagery acquired by a low-cost consumer grade unmanned aerial system (UAS). The results provide clear illustration of the systematic bowling effect following self-calibration during bundle adjustment. This was due to poor estimations of distortion parameters in the camera model. Deformation was most pronounced when UAS-GPS data were used for georeferencing. The use of dGPS-determined ground control points improved the DSM, but did not fully mitigate the deformations. By introducing a pre-calibrated model, derived using a typical checkerboard routine, deformation was significantly mitigated. These results were tested in both the commercial Agisoft PhotoScan® and open-source Micmac software. When self-calibration was used, Micmac generated significantly more accurate DSMs because a more complex lens distortion model could be implemented. The results show that when mapping flat topographies, pre-calibration of the camera model out-performs self-calibration. However, if pre-calibration is not possible, a complex distortion model (such as Micmac’s Four model) can be utilised to limit deformation. The results of the software analysis concluded there is no one-size fits all software solution, and therefore customisable open-source systems offer many potential benefits.

# Cite

```
@article{griffiths2019comparison,
  title={Comparison of pre-and self-calibrated camera calibration models for UAS-derived nadir imagery for a SfM application},
  author={Griffiths, David and Burningham, Helene},
  journal={Progress in physical geography: earth and environment},
  volume={43},
  number={2},
  pages={215--235},
  year={2019},
  publisher={SAGE Publications Sage UK: London, England}
}
```