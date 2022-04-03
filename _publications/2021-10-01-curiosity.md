---
title: Curiosity-driven 3D Object Detection without Labels
authors: <b>David Griffiths</b>, Jan Boehm, Tobias Ritschel
collection: publications
permalink: /publication/curiosity-driven
excerpt: A novel method for self-supervised monocular 3D object detection. This is achieved through differentiable rendering and a GAN-like critic loss.
date: 2021-10-01
year: 2021
venue: International Conference on 3D Vision (3DV)
paperurl: https://arxiv.org/pdf/2012.01230.pdf
teaser: '3d-curiosity.png'
---

![](/images/publications/3d_curiosity_concept.png)

# Abstract

In this paper we set out to solve the task of 6-DOF 3D object detection from 2D images, where the only supervision is a geometric representation of the objects we aim to find. In doing so, we remove the need for 6-DOF labels (i.e. position  orientation etc.), allowing our network to be trained on unlabeled images in a self-supervised manner. We achieve this through a neural network which learns an explicit scene parameterization which is subsequently passed into a differentiable renderer. We analyze why analysis-by-synthesis-like losses for supervision of 3D scene structure using differentiable rendering is not practical, as it almost always gets stuck in local minima of visual ambiguities. This can be overcome by a novel form of training, where an additional network is employed to steer the optimization itself to explore the entire parameter space i.e. to be curious, and hence, to resolve those ambiguities and find workable minima.

# Cite

```
@inproceedings{griffiths2021curiosity,
  title={Curiosity-driven 3D Object Detection Without Labels},
  author={Griffiths, David and Boehm, Jan and Ritschel, Tobias},
  booktitle={2021 International Conference on 3D Vision (3DV)},
  pages={525--534},
  year={2021},
  organization={IEEE}
}
```