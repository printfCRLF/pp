import numpy as np
import matplotlib.pyplot as plt


sample_distances = np.array([27143.88628178,  27087.98325817,  27580.04229165,  27113.1083337,
                             27057.40721048,  26693.19226411,  26916.87962035,  27229.72020211,
                             26755.77703262,  26994.32512326,  26863.90989702,  26885.76359407,
                             27055.16802439,  26846.50278894,  26761.62724163,  27011.92714,
                             27006.0414866,  27112.55543553,  27075.29318558,  27241.03510749,
                             26886.05773059,  26853.25717425,  27356.50242839,  27083.71944651,
                             27048.1317373,  26833.17214224,  27187.1114273,  26792.09492182,
                             27327.65334315,  26905.32791217,  26965.08045969,  26781.97735558,
                             27001.76307178,  26457.73102378,  27104.47241451,  27039.42276518,
                             26984.93044729,  27015.64782321,  26734.91971513,  26917.33608426,
                             27018.00056773,  26687.14839143,  27339.65512105,  26999.48176249,
                             27232.23332988,  27055.67780598,  26558.44932455,  26853.1677454,
                             26801.88222348,  26861.18523779,  26801.07982206,  27313.85177827,
                             27028.90702211,  27134.47888438,  27184.32863559,  26655.06969382,
                             26766.95785922,  27246.58734932,  26859.90997974,  26843.13093501,
                             27453.13275985,  26873.41574937,  26878.4825768,  26822.42307365,
                             26994.9099121,  26946.60404244,  26877.97718899,  26823.59522223,
                             26901.05746475,  27042.79485155,  26678.05762212,  26815.86185253,
                             26705.87521488,  27025.03575828,  26601.45264973,  27063.85095746,
                             26873.54531063,  26962.82916206,  27075.37369548,  27084.79512368,
                             26864.61856166,  27223.18632238,  26557.40113102,  26995.79204744,
                             26917.01806731,  26749.54338877,  26600.2621505,  26919.74101142,
                             27092.700555,  26977.8727147,  26849.13471473,  26524.28234783,
                             26903.92055912,  26957.90186854,  27053.1976854,  27113.30038626,
                             26833.69061488,  26980.32286769,  27457.87472776,  26607.4298234,
                             27120.50297762,  26813.97549293,  27119.1785466,  26990.11041907,
                             26753.55181914,  26525.20469951,  26842.72974227,  26973.67981323,
                             26644.18669416,  27335.23537165,  26974.77143351,  27114.95839037,
                             26858.96264682,  26835.49786595,  26531.37432824,  27126.72630558,
                             26913.79981063,  26860.88065597,  27238.26729004,  26903.87271231,
                             27513.09247822,  26548.8345489,  26999.26166747,  27057.7189009,
                             26855.09506965,  26846.60168945,  26998.49380647,  26681.04629384,
                             27053.79099607,  26496.07750486,  27036.1456002,  27016.92252596,
                             26481.37833241,  27463.50952723,  26941.62131814,  26709.51469047,
                             26566.83038974,  27183.90514637,  26857.18592379,  26890.57821981,
                             27297.38075903,  27182.21187189,  27007.75242303,  26745.98219617,
                             26604.88487869,  27265.42925406,  26966.86884722,  26737.8827,
                             26861.68486165,  27100.295441,  27187.91639576,  27244.33375738,
                             26785.46575254,  26596.83571684,  26634.24093179,  26977.26170876,
                             26837.52656605,  27161.00628236,  26824.60504805,  26818.95578474,
                             26933.79406034,  26746.69702688,  26992.12439671,  26594.40884625,
                             27136.65457708,  27006.47774178,  27348.6312121,  26640.05169387,
                             26714.48926311,  26976.750765,  26891.78137871,  27415.10567461,
                             26863.34205649,  26864.13041363,  26933.87284308,  27240.9018238,
                             26780.34584953,  27101.21398455,  26536.27695868,  27205.70198053,
                             26766.53883905,  26828.57836298,  26995.50842643,  26714.33520856,
                             26850.33271654,  27351.41721953,  26804.22626971,  26654.90293713,
                             27304.44206032,  26847.36626491,  26804.55720083,  26829.07844477,
                             26764.00163473,  27052.12291217,  26567.20279511,  26960.61254516,
                             27065.57672416,  26744.10077992,  27314.71742361,  26663.42154431,
                             26970.9819719,  26694.67840398,  26996.04004449,  26801.79974578,
                             27061.01623074,  26937.19018333,  26857.45686715,  26593.49519935,
                             26716.65215727,  27010.58406499,  27054.09857263,  26944.52372485,
                             26878.21290192,  26989.57495373,  27096.37064746,  26716.88817842,
                             26836.57256623,  27033.67598741,  26863.87803964,  27047.20798789,
                             27034.91369359,  26685.87451072,  27039.83885243,  26791.89970318,
                             26849.33668429,  27026.34834406,  26695.23683922,  26904.80471305,
                             26436.85015118,  26830.81472121,  26911.67043354,  27404.79981318,
                             26957.87969301,  27033.96423562,  26957.63539671,  26771.38920367,
                             27258.24706918,  26968.81217189,  27199.03755538,  26961.52942659,
                             26739.94237613,  27134.65276966,  26630.07179143,  26754.10986303,
                             26734.2688266,  26955.89986361,  26980.93876681,  26780.9502099,
                             26881.43697313,  26861.55370871,  26938.04451192,  27424.71030759,
                             27224.90782133,  27567.66884372,  26942.45666815,  26666.49862448,
                             26811.51215308,  26862.3358439,  26990.77460817,  26724.01040161,
                             26716.03660602,  27089.57059653,  27089.43869505,  26738.7977659,
                             26639.01975494,  26732.8054403,  27148.6025703,  26772.1406178,
                             26823.98368548,  26944.55993598,  26899.06286655,  27274.75301706,
                             26732.66097594,  27078.97928512,  27156.28365114,  26674.92376282,
                             26591.16650517,  26901.28578514,  26854.2124564,  26637.76152564,
                             27067.74816302,  26977.5439568,  26938.91884692,  27056.15166122,
                             26905.21037053,  26887.87603461,  26618.12393823,  26842.1454847,
                             27243.69949251,  27019.77978195,  27024.08660277,  26942.38510255,
                             26855.35443262,  26486.76635941,  26514.29446274,  26886.15161863,
                             26585.50047227,  26654.4768983,  26991.29015812,  27157.85397661,
                             26933.96043703,  26890.65691518,  27238.72323288,  26805.130186,
                             27125.58144028,  27327.70213603,  27171.75239724,  27093.72863873,
                             26587.66972079,  26617.52797802,  26821.20198502,  26857.73533964,
                             26635.38737764,  26661.90040372,  26829.5779198,  26741.62947342,
                             27190.30556829,  26579.22864091,  27497.96834736,  27081.02355063,
                             26769.52914657,  26985.74574184,  27595.80878556,  26487.11507164,
                             27292.42142024,  26733.38001826,  26648.9204039,  27429.34320411,
                             26843.95841763,  26892.15101573,  26822.53694383,  26475.39327269,
                             26981.99259762,  26764.28248029,  27077.40025535,  26873.83834394,
                             27194.15938715,  26953.27264372,  26964.84608336,  27080.18180957,
                             26683.31744167,  26502.83895785,  26844.16395718,  27134.59783351,
                             26990.62775284,  26922.07725332,  27190.05269203,  27065.33499104,
                             27268.61508165,  26512.11430426,  26612.70415815,  26942.6117626,
                             26785.98958143,  26879.59951891,  27074.25111081,  26638.0334235,
                             26858.27340454,  27265.22585654,  26731.03040891,  26706.0906174,
                             26881.98394737,  27076.9711286,  27072.06023771,  27172.94087273,
                             26860.60951111,  26637.69630775,  26921.5832547,  26868.06131472,
                             26600.09476209,  26660.55416077,  26615.43446626,  26834.83778753,
                             27068.60120026,  26916.29208527,  26988.51212715,  26825.589366,
                             27010.21997456,  26767.49717399,  26582.69461741,  26654.01298353,
                             26878.09411344,  26842.16941808,  26769.71400851,  26793.55753181,
                             26780.7725181,  26832.16520869,  26520.33080082,  26878.99396777,
                             26626.28412691,  26836.54178272,  26747.54469582,  27325.33127661,
                             27000.43140943,  26591.54085344,  27050.44515082,  26819.78852642,
                             26768.79271964,  26623.20005054,  26499.24012889,  27034.55732796,
                             26972.30548523,  27076.97833476,  27145.97653883,  27370.45045816,
                             26788.54262976,  27185.12908371,  27105.10953604,  26633.87050673,
                             26497.62446903,  26629.59429991,  27303.09765554,  27512.90634296,
                             26979.4130203,  27288.31979692,  26775.90921763,  27246.3093449,
                             26702.97967346,  27127.80327595,  26887.79015222,  26845.61680541,
                             27325.07216057,  26912.04092278,  26698.64746013,  27069.89578735,
                             26896.89216195,  26825.16825668,  26719.23253875,  27089.1351968,
                             26907.17017392,  26615.46233873,  26647.44351774,  26882.2284668,
                             26873.25430701,  27131.32632721,  26561.99089323,  26896.45048256,
                             26779.47437051,  26866.97946212,  26580.68558289,  26866.31573419,
                             26942.87693368,  26575.09935991,  26895.31801405,  26927.33675451,
                             27097.5658296,  27128.16478439,  26405.45893621,  26994.71552069,
                             27063.31273634,  26748.21332282,  26808.8932871,  26724.7750947,
                             26886.51488927,  26505.51673261,  26998.04607751,  26816.22792519,
                             26849.55072425,  26826.30312419,  27380.98648648,  27001.70154691,
                             26945.59491929,  26892.01594966,  27008.94931909,  27216.56367404,
                             26780.61753675,  27085.16847858,  27309.98648719,  27024.33210759,
                             26696.51722235,  26885.77145915,  27091.30918844,  27288.44923661,
                             26843.78490903,  26995.37811275,  27138.50850968,  27075.52853479,
                             26788.01558595,  26686.5137108,  26907.76987956,  27043.41094828,
                             27002.33688256,  27000.58628711,  26923.24546555,  26992.01623444,
                             26839.18921918,  26876.01983098,  26824.33127226,  26670.56916053,
                             27171.51413067,  26223.68323013,  27181.98404,  26803.87711263,
                             27103.321864,  27095.93537004,  26770.49982931,  27057.20228503,
                             27221.60761577,  27094.98258615,  27115.18560631,  26842.77894778,
                             27323.4894849,  26881.86334618,  26837.51410218,  27130.37924233,
                             26660.94358069,  26731.11198984,  26905.96625456,  26789.17451613,
                             26934.47552903,  26695.9977087,  26951.91390559,  26930.80109208,
                             26650.40867341,  27314.64800395,  26801.46760827,  27087.49867632,
                             26630.66491592,  26918.4092305,  26953.25107897,  26717.30404149,
                             26949.66946678,  26754.97063429,  26870.10207066,  26807.38876625,
                             27107.55234701,  26601.59319672,  26821.24022814,  26685.63552257,
                             27044.86820473,  27416.09728796,  26677.99084544,  26854.67530358,
                             26786.93680732,  27010.23095439,  27232.56444479,  26887.24710797,
                             26680.41523995,  26834.47744991,  27062.41793769,  26763.82670317,
                             26935.17919968,  27100.28799049,  26698.32757744,  27198.96478924,
                             26650.21345545,  26887.53157538,  26814.57686748,  26605.44529358,
                             27215.91089759,  26685.02505006,  26807.00356023,  27183.35159978,
                             27299.01025863,  26540.3273963,  27014.04664468,  27182.21812316,
                             26767.58852115,  27009.07760766,  26723.04531565,  27017.79895826,
                             26768.65088691,  26777.76464446,  26315.61040777,  27133.86367531,
                             26918.66726152,  26853.81704745,  27347.05391,  26766.18432387,
                             26960.80182685,  26988.449127,  26876.66140718,  26939.05893723,
                             26982.01789116,  26919.20819375,  26747.81346849,  26717.85402756,
                             26739.96859867,  27046.28760018,  26679.84821861,  26675.41876112,
                             26896.86351377,  26834.36394749,  27025.01206036,  26832.62404834,
                             26796.37376438,  26722.27745533,  26604.57505423,  26874.84134077,
                             26709.89006538,  26647.86223725,  27365.60478048,  27250.48206328,
                             26943.0014568,  26681.2406666,  26908.14576762,  26768.46801898,
                             26704.72233385,  27395.07225842,  26555.49997708,  26920.70572279,
                             26787.9513203,  26621.50935879,  27023.69869608,  26983.26169904,
                             27051.78206884,  26924.32570734,  27221.81159283,  27041.46242069,
                             26893.2471373,  26620.10418654,  26803.4755538,  27110.75619235,
                             26971.28591253,  27004.02059281,  26482.00284554,  26667.06080455,
                             26796.77272328,  27053.93552085,  26917.11701927,  26742.88375437,
                             26597.94705253,  26947.42274881,  26702.75921747,  26960.44887525,
                             27066.83062975,  26638.57233818,  26636.88207672,  27326.19853941,
                             26900.83561322,  26931.97729053,  26599.46245532,  27348.70514627,
                             26950.12066067,  26695.35062517,  26729.06808538,  26998.34292279,
                             27019.78429031,  26763.23333842,  27147.21522235,  26754.26076967,
                             26655.98520353,  27086.3651111,  26652.40607143,  27091.7757577,
                             27062.96184973,  27105.95015082,  26792.60176359,  27127.00319873,
                             27050.079599,  26845.32238507,  27226.1787699,  26931.21354275,
                             26680.03663918,  26945.87861519,  27201.82207787,  26941.14577377,
                             26893.08110167,  26805.7467604,  27194.65948651,  26793.96677552,
                             27206.19599613,  27224.62796493,  26875.27332831,  27283.97611498,
                             26983.48649331,  27219.68903172,  27052.57102147,  26933.15409584,
                             27139.31217806,  26976.22048026,  26774.99891765,  26942.74073873,
                             27038.3178845,  27087.09341814,  26995.69255902,  26946.14042527,
                             26903.47898471,  26733.12804219,  27300.39468856,  27033.12914345,
                             27234.96606573,  27323.80585794,  27321.96344636,  26843.46999031,
                             26674.17193316,  26972.83513715,  27146.64170615,  26489.85474017,
                             27210.57478495,  27165.28016939,  27195.45813929,  26727.86490468,
                             27104.78719821,  27051.34953546,  26836.93814066,  26592.54776213,
                             26703.80227206,  26855.44832291,  26593.15487319,  26671.55142006,
                             27236.79514512,  27169.13090286,  27250.99331408,  26833.65624651,
                             26943.85545535,  26832.80716137,  26777.88560215,  26914.76627881,
                             27097.62559952,  26963.72096872,  26797.53748958,  26941.24868294,
                             26658.10570875,  26719.42705881,  27128.30406468,  27038.41144606,
                             26989.98023337,  26780.44553277,  26643.26778624,  27122.50113836,
                             26820.2468365,  26743.371561,  26625.22120759,  26910.22885212,
                             26676.67434759,  26931.08841229,  27028.30751521,  26715.73606702,
                             27097.83048853,  26752.17630407,  26671.09756155,  26755.26600278,
                             26370.7931108,  26928.53647969,  27075.80042784,  26578.35985294,
                             27002.0644265,  27019.44718263,  26924.43204291,  27396.64607862,
                             27166.88130204,  26738.05290813,  26911.29195765,  26870.85296559,
                             26996.29539281,  27051.67225526,  26675.14343869,  26936.77477091,
                             26994.14449431,  26636.99318269,  26754.42383871,  26852.07254784,
                             27023.25751189,  27078.57722094,  26665.21185785,  27378.73907689,
                             26990.43019433,  27042.00311502,  26535.25252992,  27217.66345914,
                             26864.36032814,  26728.99675236,  26810.25495155,  27081.33425362,
                             26610.70127851,  26750.27968439,  26660.33556415,  26502.09070115,
                             26759.74644598,  26331.88707073,  26953.62290489,  27225.54555162,
                             26803.85604939,  27015.80260236,  27063.97236074,  27385.62714809,
                             27314.66456811,  26605.24572727,  27196.06336614,  26540.36402604,
                             26714.60999015,  27070.9127378,  26624.93717501,  26768.40846424,
                             26654.76203627,  26499.09780301,  26631.22707081,  26920.58225453,
                             26877.40880054,  27082.2237341,  26827.86981599,  27183.80817945,
                             27254.65759647,  26986.3498665,  26891.20102975,  26772.17730581,
                             27022.56291652,  27222.27181425,  27032.95585834,  26425.61520155,
                             26990.75731642,  27025.2380441,  27350.73641571,  26586.64903611,
                             26649.97317418,  27111.79872903,  26925.84914513,  26846.22885122,
                             27101.85249399,  26902.73954691,  26984.05823343,  27023.62942578,
                             27034.21271529,  27017.04554648,  26768.6557724,  26518.5160293,
                             26836.093973,  27304.38452298,  27475.42373782,  26828.68336861,
                             26861.25909624,  26845.25731839,  26656.6082006,  27407.50248621,
                             27059.52042785,  26616.03753249,  26557.44125806,  26943.8869675,
                             26898.74692024,  26994.91799687,  27083.65141568,  27085.82309686,
                             26841.77912625,  27103.62403982,  27343.12373789,  26845.49505206,
                             26532.02269793,  27032.98876105,  27053.56903534,  27411.25022777,
                             27029.58842804,  26929.58851687,  26818.69960195,  27306.97990886,
                             26495.64048647,  26792.38926062,  26833.75249299,  26909.81195161,
                             27208.8970663,  26952.93021651,  27031.57025867,  26887.10128666,
                             26771.66893823,  26523.07005484,  27362.29681554,  26927.53837938,
                             26917.88028539,  26900.10269084,  27240.5227911,  27081.44638233,
                             26677.93446405,  26917.97260646,  26836.60271979,  26461.22083287,
                             27281.22945966,  27273.74150261,  26976.44476805,  26875.84043766,
                             27106.3293943,  26799.52335095,  27007.24644262,  26665.16966301,
                             27304.18394391,  27274.59688309,  26698.09233131,  26791.34443134,
                             26933.52542265,  27092.15719432,  27459.08034851,  26978.15558848,
                             26720.64676711,  27305.78954085,  26858.61814665,  26297.59172422,
                             26943.93494132,  26793.18115764,  26675.93582648,  27329.56087595,
                             26623.85064432,  26954.93895181,  27006.99634429,  26972.19643487,
                             26548.91205334,  26700.5882683,  27218.44546661,  26653.55229226,
                             26677.28514474,  26748.3959728,  26915.79737455,  27158.97192811,
                             27290.58173574,  27086.98581331,  27006.43260782,  27106.01510998,
                             26701.22838215,  26578.52101416,  26722.69176413,  27027.26101764,
                             26762.08980586,  27096.09446463,  26943.22569795,  26505.59147123,
                             26863.34213189,  26494.20132514,  26753.72611516,  26778.60980042,
                             27008.33743502,  26985.91717751,  26615.82439677,  26866.19639427,
                             27206.61338108,  26607.41840873,  26832.85939927,  26838.13637565,
                             26850.27608958,  26713.03256229,  27093.70907553,  26728.60490451,
                             26721.61336247,  26856.95405826,  26780.65391093,  27152.90060359,
                             27065.71310498,  26868.56348521,  26870.46747994,  27160.40631194,
                             26603.45129763,  27164.29835919,  27050.25504941,  27038.57219125,
                             27114.21399491,  27015.82602835,  26782.83405673,  27119.42172252,
                             27207.79904991,  27087.54947541,  26697.06522995,  27025.00358675,
                             27463.94277955,  27439.92924195,  26758.2418425,  27170.83196079,
                             27004.1265311,  26973.39457052,  26824.44913799,  26887.24803323,
                             26540.11143709,  26977.01335687,  27026.48820243,  26876.57197134,
                             26961.04725683,  26774.41004752,  27028.82952681,  26884.38731073,
                             26917.86490144,  27221.46739035,  26567.3547064,  27437.83066131,
                             27007.37053409,  26934.79679098,  26828.67647402,  26918.02157083,
                             27102.91594912,  26926.21346822,  26703.24071232,  26752.40561732,
                             26910.72499058,  27073.01916917,  26714.79735407,  27113.196917,
                             26925.71162521,  27427.67784218,  27051.8207997,  26884.4680432,
                             26856.70934044,  27114.99783882,  26937.11394529,  26952.30554279,
                             26733.23494685,  27091.61448119,  27192.92226796,  27068.805274,
                             26347.87498413,  27106.86164021,  26970.13665055,  26279.50028187,
                             26497.08684322,  27254.38245243,  26942.48399784,  26898.40060351])


def gaussian_model(x, mu, sigma):
    return 1/(np.sqrt(2 * np.pi * sigma**2)) * np.exp(- (x - mu)**2 / (2 * sigma**2))


def plot_data_and_model(data, model, opt_sort=False):
    data_bins = np.linspace(np.min(data), np.max(data), 21)
    data_opts = dict(rwidth=0.8, color='black', alpha=0.25)
    model_opts = dict(linewidth=4, color='red', alpha=0.5,
                      linestyle=' ', marker=".")
    if opt_sort:
        # Note: Critical thing students get wrong a LOT!
        # By default, we turn off linestyle, which connects-the-dots in order
        # This is bad here, because the data and model are not sorted in order of increasing distance
        # Sorting only the data or only the model, by size, will break everything,
        # since the model and data are connected point-by-point, they both must be sorted together
        # Here we sort by data (distance)
        sort_indices = np.argsort(data)
        data = data[sort_indices]
        model = model[sort_indices]
        model_opts = dict(linewidth=4, color='red',
                          alpha=0.5, linestyle='-', marker=".")
    font_options = {'family': 'Arial', 'size': 16}
    plt.rc('font', **font_options)
    fig, axis = plt.subplots(figsize=(12, 8))
    count, bins, patches = axis.hist(
        data, data_bins, density=True, cumulative=False, label='data', **data_opts)
    line = axis.plot(data, model, label='model', **model_opts)
    axis.grid()
    axis.set_ylabel("Population vs Sample")
    axis.set_xlabel("Distance")
    axis.legend()
    # title = axis.set_title('Guassian model, mu = {:0.1f}, sigma = {:0.1f}'.format(mu, sigma))
    title = axis.set_title('Data and Model')
    fig.tight_layout()
    plt.show()
    return fig


def compute_loglikelihood(samples, mu, sigma=250):
    probs = np.zeros(len(samples))
    for n, sample in enumerate(samples):
        probs[n] = gaussian_model(sample, mu, sigma)
    loglikelihood = np.sum(np.log(probs))
    return loglikelihood


def compute_loglikelihood(samples, mu, sigma=250):
    probs = np.zeros(len(samples))
    for n, sample in enumerate(samples):
        probs[n] = gaussian_model(sample, mu, sigma)
    loglikelihood = np.sum(np.log(probs))
    return loglikelihood


def plot_loglikelihoods(mu_guesses, loglikelihoods):
    max_loglikelihood = np.max(loglikelihoods)
    max_index = np.where(loglikelihoods == max_loglikelihood)
    max_guess = mu_guesses[max_index][0]
    font_options = {'family': 'Arial', 'size': 16}
    plt.rc('font', **font_options)
    fig, axis = plt.subplots(figsize=(10, 6))
    axis.plot(mu_guesses, loglikelihoods)
    axis.plot(max_guess, max_loglikelihood, marker="o", color="red")
    axis.grid()
    axis.set_ylabel('Log Likelihoods')
    axis.set_xlabel('Guesses for Mu')
    axis.set_title('Max Log Likelihood = {:0.1f} \n was found at Mu = {:0.1f}'.format(
        max_loglikelihood, max_guess))
    fig.tight_layout()
    plt.show()
    return fig


def estimation_of_population_parameters():
    # Compute the mean and standard deviation of the sample_distances
    sample_mean = np.mean(sample_distances)
    sample_stdev = np.std(sample_distances)

    # Use the sample mean and stdev as estimates of the population model parameters mu and sigma
    population_model = gaussian_model(
        sample_distances, mu=sample_mean, sigma=sample_stdev)

    # Plot the model and data to see how they compare
    fig = plot_data_and_model(sample_distances, population_model)


def maximizing_likelihood():
    # Compute the mean and standard deviation of the sample_distances
    sample_mean = np.mean(sample_distances)
    sample_stdev = np.std(sample_distances)

    # Compute sample mean and stdev, for use as model parameter value guesses
    mu_guess = np.mean(sample_distances)
    sigma_guess = np.std(sample_distances)

    # For each sample distance, compute the probability modeled by the parameter guesses
    probs = np.zeros(len(sample_distances))
    for n, distance in enumerate(sample_distances):
        probs[n] = gaussian_model(distance, mu=mu_guess, sigma=sigma_guess)

    # Compute and print the log-likelihood as the sum() of the log() of the probabilities
    loglikelihood = np.sum(np.log(probs))
    print('For guesses mu={:0.2f} and sigma={:0.2f}, the loglikelihood={:0.2f}'.format(
        mu_guess, sigma_guess, loglikelihood))

    # Create an array of mu guesses, centered on sample_mean, spread out +/- by sample_stdev
    low_guess = sample_mean - 2*sample_stdev
    high_guess = sample_mean + 2*sample_stdev
    mu_guesses = np.linspace(low_guess, high_guess, 101)

    # Compute the loglikelihood for each model created from each guess value
    loglikelihoods = np.zeros(len(mu_guesses))
    for n, mu_guess in enumerate(mu_guesses):
        loglikelihoods[n] = compute_loglikelihood(
            sample_distances, mu=mu_guess, sigma=sample_stdev)

    # Find the best guess by using logical indexing, the print and plot the result
    best_mu = mu_guesses[loglikelihoods == np.max(loglikelihoods)]
    print('Maximum loglikelihood found for best mu guess={}'.format(best_mu))
    fig = plot_loglikelihoods(mu_guesses, loglikelihoods)

# estimation_of_population_parameters()
maximizing_likelihood()
