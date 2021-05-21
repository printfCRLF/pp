import numpy as np

sample_data = np.array([-2.56528602e-01,   1.33537708e+00,   3.10605971e+00,
                        -3.88306749e-01,  -3.68273914e-01,   3.27842563e+00,
                        1.67486946e+00,  -7.78948772e-01,   1.26512009e+00,
                        -7.26835386e-01,  -7.11459507e-01,   7.23924543e-01,
                        -3.56656049e+00,  -3.16983567e+00,  -8.24575058e-01,
                        -1.70566224e+00,   9.68494665e-01,  -1.45604815e+00,
                        -2.44460740e+00,   3.33129754e+00,  -3.15526010e-02,
                        5.75056409e-01,  -2.38949637e+00,  -6.08765449e-01,
                        7.21845179e-01,  -1.78198715e+00,   1.29139604e+00,
                        -6.41277380e-01,  -3.38749959e-03,  -6.03413224e-01,
                        4.32455637e+00,   6.13005551e-01,  -1.45542186e+00,
                        2.32508982e+00,  -1.74168730e+00,   1.13772719e+00,
                        -3.17934025e+00,  -1.89637210e+00,   1.17372247e+00,
                        2.27693316e+00,   1.16273656e+00,   6.08703435e-01,
                        2.57792609e-01,  -2.07704398e+00,  -5.39688417e-01,
                        -1.27754192e-03,   3.05424445e+00,   1.64723658e+00,
                        -2.54608031e+00,   1.64816794e+00,   2.49835439e-01,
                        -3.13844001e-01,   2.28335258e+00,   3.14199904e+00,
                        2.96256024e+00,  -5.58435046e-01,   5.21575248e-01,
                        1.82252686e+00,   3.13109025e+00,   2.41651524e-01,
                        8.48682047e-01,  -9.72669948e-01,  -1.13241325e+00,
                        2.90505164e+00,   4.01248006e+00,   1.17597976e+00,
                        3.34706580e+00,   2.08327205e+00,   8.97604908e-02,
                        2.12279121e+00,   4.49607313e+00,   1.36834792e+00,
                        4.58928731e+00,  -3.75949021e+00,   3.14380501e+00,
                        1.69409414e+00,   9.41985299e-01,   1.74352155e+00,
                        -2.39513783e+00,   1.16065622e+00,   2.33422514e+00,
                        4.59578809e+00,   6.23459563e-01,   6.30127942e-02,
                        6.96485913e-01,   3.55080424e+00,   2.39750222e+00,
                        7.00479592e-01,   2.80653487e+00,   1.99415510e+00,
                        3.75728998e+00,   4.35893812e-01,   1.20467571e+00,
                        1.09578369e+00,  -1.02702990e+00,   2.51224055e+00,
                        2.46211054e+00,   1.97022691e+00,   1.51082573e+00,
                        -8.30741484e-01,   1.17870935e+00,   1.35457097e+00,
                        4.55445462e-01,   1.75742858e+00,   2.90810171e+00,
                        5.89237180e+00,   2.48915563e+00,   2.67510078e+00,
                        2.03110817e+00,  -1.63754243e+00,   2.16697225e+00,
                        2.36046042e+00,   7.18648422e+00,   1.89527807e+00,
                        2.90309468e+00,   2.25057646e+00,   2.64392476e-03,
                        4.64564563e+00,   3.88386607e+00,   3.98206389e+00,
                        6.01225090e-01,   5.24558862e+00,  -3.43702126e-01,
                        3.65371419e+00,   6.88091125e+00,   5.38927350e-01,
                        1.40740454e+00,   2.75930273e+00,   1.57304869e+00,
                        -5.01326862e-01,   2.75712595e+00,   5.15392573e-01,
                        3.60718486e+00,   8.41151532e-01,   5.79986881e+00,
                        1.15349342e+00,   2.09587697e+00,   4.38703443e+00,
                        3.18271367e-01,   3.25491987e+00,   5.43428551e+00,
                        -3.74966469e-01,   3.22926772e+00,   3.39976559e+00,
                        4.46364574e+00,   4.46098578e-01,   2.99086774e-01,
                        4.00388313e+00,   3.57396935e+00,   3.50098570e+00,
                        3.71289642e+00,   1.67995056e+00,   3.52450739e+00,
                        3.66614495e+00,   1.67129716e+00,   6.85154902e+00,
                        4.08766584e+00,   7.77393006e-01,   4.49310722e+00,
                        1.25063666e+00,   4.79416921e+00,   5.55719116e+00,
                        1.61863536e+00,   5.20675226e+00,   4.12556185e+00,
                        4.96412032e+00,   7.13358597e+00,   2.86922377e+00,
                        1.87252767e+00,   1.62097114e+00,   1.78837943e+00,
                        3.28579658e+00,   4.14230395e+00,   4.03338160e+00,
                        5.15436650e+00,   3.54600378e+00,   6.44706815e+00,
                        3.03068633e+00,   9.02033833e+00,   4.85133470e+00,
                        1.90568489e+00,   1.49821500e+00,   4.62494483e+00,
                        3.23307443e+00,   5.12800099e+00,   4.66647525e+00,
                        3.59434217e+00,   2.06641256e+00,   7.50305551e-01,
                        2.90697010e+00,   5.53279759e+00,   4.26818749e+00,
                        1.36852244e+00,   4.22636185e+00,   4.67063476e+00,
                        2.15228513e+00,   4.24745021e+00,   4.07641744e+00,
                        1.69405940e+00,   4.71557472e+00,   5.14156905e+00,
                        6.20610249e+00,   6.16760410e+00,   1.32466126e+00,
                        2.22434992e+00,   5.15007053e+00,   5.16757190e+00,
                        5.19009537e+00,   1.18854630e+01,   5.34178102e+00,
                        6.49113128e+00,   6.14800353e+00,   5.56278250e+00,
                        3.64946151e+00,   5.81793844e+00,   2.77434957e+00,
                        3.86636279e+00,   3.38927290e+00,   4.54374828e+00,
                        9.02931713e+00,   6.85469615e-01,   5.81252038e+00,
                        1.23456826e+00,   3.53613627e+00,   6.67790119e+00,
                        4.64856004e+00,   2.38451044e+00,   3.12939258e+00,
                        5.93919550e+00,   3.13926674e+00,   5.05291718e+00,
                        4.73114368e+00,   3.35679930e+00,   8.96788818e+00,
                        5.96783804e+00,   6.69714827e-01,   5.11290863e+00,
                        3.43642707e+00,   6.48486667e+00,   3.21495852e+00,
                        4.59052712e+00,   5.84997456e+00,   6.59151039e+00,
                        2.47940719e+00,   4.23099753e+00,   3.97010938e+00,
                        3.63334153e+00,   8.49090848e+00,   5.78996342e+00,
                        2.47823209e+00,   6.85572389e+00,   9.28431239e+00,
                        7.12493052e+00,   2.04126007e+00,   4.13153185e+00,
                        7.65382230e+00,   3.72466107e+00,   6.04763886e+00,
                        6.72926811e+00,   3.34613906e+00,   5.10094929e+00,
                        -1.24253468e+00,   3.21122472e+00,   4.77486370e+00,
                        2.80443364e+00,   8.58482261e+00,   2.47971724e+00,
                        4.47991103e+00,   5.64148115e+00,   8.28254658e+00,
                        2.54827570e+00,   7.76632750e+00,   5.48046612e+00,
                        3.51698270e+00,   6.42420695e+00,   5.91811939e+00,
                        4.33956625e+00,   5.69960417e+00,   4.80937281e+00,
                        5.82703469e+00,   6.94426135e+00,   8.81203363e+00,
                        3.18436900e+00,   9.94606675e+00,   1.79582440e+00,
                        5.41642981e+00,   6.91663441e+00,   6.32198374e+00,
                        4.53460096e+00,   5.38375550e+00,   4.83399813e+00,
                        4.66127049e+00,   7.55920419e+00,   6.59403097e+00,
                        4.51418081e+00,   7.71919975e+00,   6.55459904e+00,
                        7.58572424e+00,   7.23925768e+00,   4.34200998e+00,
                        4.89963792e+00,   7.53458721e+00,   7.28074053e+00,
                        6.03819681e+00,   6.33465477e+00,   8.67532979e+00,
                        4.95685722e+00,   7.25419476e+00,   5.77561470e+00,
                        5.76463759e+00,   8.41755370e+00,   7.89083270e+00,
                        7.88701927e+00,   8.89095761e+00,   6.34200768e+00,
                        7.68390594e+00,   5.71946649e+00,   7.00833270e+00,
                        6.11971389e+00,   6.59399193e+00,   7.61031405e+00,
                        4.80355863e+00,   1.06447746e+01,   4.46796524e+00,
                        4.07162277e+00,   8.83622175e+00,   8.12332539e+00,
                        7.80823963e+00,   7.83669102e+00,   6.57550645e+00,
                        4.82549126e+00,   6.79160912e+00,   5.30567658e+00,
                        8.63023947e+00,   6.40588524e+00,   5.06900561e+00,
                        6.09722832e+00,   7.58586291e+00,   5.65255089e+00,
                        5.15555921e+00,   7.30737442e+00,   7.32993314e+00,
                        5.84611365e+00,   5.93792339e+00,   7.36409987e+00,
                        4.02383132e+00,   4.12507245e+00,   5.52311156e+00,
                        6.55310570e+00,   7.62181513e+00,   9.97071243e+00,
                        8.75531925e+00,   6.74012294e+00,   7.04196758e+00,
                        5.09494127e+00,   7.08297373e+00,   6.56268272e+00,
                        7.80543712e+00,   5.52553811e+00,   8.23869303e+00,
                        1.02854778e+01,   7.02247970e+00,   8.06342344e+00,
                        8.66028798e+00,   6.49755906e+00,   7.76818496e+00,
                        7.36518480e+00,   7.55535220e+00,   5.83398043e+00,
                        7.44902035e+00,   8.41599658e+00,   1.03422872e+01,
                        9.37854165e+00,   1.17863649e+01,   5.96530487e+00,
                        9.26464127e+00,   7.90668401e+00,   1.19396059e+01,
                        5.96340343e+00,   5.92055632e+00,   6.42121471e+00,
                        3.39220855e+00,   6.60848996e+00,   6.16173468e+00,
                        8.00078757e+00,   8.40351195e+00,   1.14923417e+01,
                        9.66084768e+00,   6.62619269e+00,   6.00317066e+00,
                        8.80383834e+00,   5.19953359e+00,   1.15229175e+01,
                        1.02388802e+01,   6.96164870e+00,   4.49373094e+00,
                        1.06477447e+01,   7.73092031e+00,   1.04556326e+01,
                        4.81114468e+00,   6.82124995e+00,   8.05048740e+00,
                        8.15396119e+00,   7.17986906e+00,   9.34569986e+00,
                        5.98475914e+00,   7.85524103e+00,   8.40059126e+00,
                        9.20887767e+00,   9.62322976e+00,   5.97071582e+00,
                        5.17177166e+00,   1.08153536e+01,   8.94462802e+00,
                        6.80302693e+00,   1.14223040e+01,   8.57134927e+00,
                        1.07185944e+01,   8.51503696e+00,   1.25214958e+01,
                        1.19306817e+01,   7.94207170e+00,   1.04031419e+01,
                        9.77075190e+00,   1.12372631e+01,   6.59015308e+00,
                        9.91210292e+00,   1.06768490e+01,   5.06252103e+00,
                        6.23348297e+00,   4.54153564e+00,   8.10118633e+00,
                        1.00950845e+01,   1.16847141e+01,   8.84818956e+00,
                        1.19772311e+01,   5.97979708e+00,   5.35323512e+00,
                        8.66890460e+00,   9.56813090e+00,   8.75461050e+00,
                        4.70511580e+00,   8.68175992e+00,   6.27106100e+00,
                        1.02393451e+01,   9.65319649e+00,   7.06024043e+00,
                        7.93226617e+00,   6.86157296e+00,   8.87464181e+00,
                        1.09302846e+01,   7.06854791e+00,   1.00680930e+01,
                        8.01948476e+00,   7.51425434e+00,   8.90593928e+00,
                        7.06951536e+00,   8.05270139e+00,   6.78424421e+00,
                        1.31294503e+01,   9.29052710e+00,   7.84054898e+00,
                        9.68795982e+00,   9.05534390e+00,   8.85806080e+00,
                        1.05483334e+01,   1.08550154e+01,   8.29899770e+00,
                        8.22836352e+00,   8.84989661e+00,   4.81615767e+00,
                        6.40961788e+00,   1.21937485e+01,   1.27699354e+01,
                        9.00192792e+00,   1.06731139e+01,   1.01625003e+01,
                        1.57177616e+01,   1.18191498e+01,   9.34416482e+00,
                        7.70891912e+00,   6.42710736e+00,   1.00669273e+01,
                        8.16729851e+00,   6.85549258e+00,   8.42685423e+00,
                        7.57690399e+00,   1.31342833e+01,   1.15432795e+01,
                        9.78405472e+00,   1.27798883e+01,   9.99473662e+00,
                        8.13743160e+00,   1.29262482e+01,   1.09778201e+01,
                        7.84550769e+00,   9.55932264e+00,   8.20876349e+00,
                        7.21440054e+00])
