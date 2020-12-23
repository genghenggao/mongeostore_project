'''
Description: henggao_learning
version: v1.0.0
Author: henggao
Date: 2020-12-16 09:08:20
LastEditors: henggao
LastEditTime: 2020-12-23 17:29:41
'''
import segyio
import numpy as np
import math as m
from matplotlib import pyplot as plt

filename = ".\mongeostore_env\mytest\LX_SEGY2.segy"
# filename = ".\SEGY\data\LX_SEGY2.segy"
# filename=".\SEGY\data\zero_merge.sgy"
with segyio.open(filename, mode="r", strict=False, ignore_geometry=False, endian='big') as f:
    # print(f.trace[3225:3226])         # <generator object Trace.__getitem__.<locals>.gen at 0x000001D562712648>
    # print(f.ilines)                   # None
    # print(f.tracecount)               # 255701
    # print(f.attributes)               # <bound method SegyFile.attributes of SegyFile('.\data\LX_SEGY2.segy', 'r', iline = 189, xline = 193)>
    # print(f.bin)
    '''
        {JobID: 1, LineNumber: 1, ReelNumber: 1, Traces: 1, AuxTraces: 0, Interval: 1000, IntervalOriginal: 0, Samples: 2001, SamplesOriginal: 0, Format: 1, 
        EnsembleFold: 1, SortingCode: 4, VerticalSum: 1, SweepFrequencyStart: 0, SweepFrequencyEnd: 0, SweepLength: 0, Sweep: 0, SweepChannel: 0, SweepTaperStart: 0, 
        SweepTaperEnd: 0, Taper: 0, CorrelatedTraces: 0, BinaryGainRecovery: 0, AmplitudeRecovery: 0, MeasurementSystem: 1, ImpulseSignalPolarity: 1, VibratoryPolarity: 0, 
        SEGYRevision: 0, TraceFlag: 0, ExtendedHeaders: 0}
    '''
    # print(f.endian)                     # big
    # print(f.depth)                      # None
    # print(f.depth_slice)                # <segyio.depth.Depth object at 0x00000214B48C3F48>
    # print(f.dtype)                      # float32
    # print(f.ext_headers)                # 0
    # print(f.close)
    # print(f.format)                     # 4-byte IBM float
    # print(f.header)                     # <segyio.trace.Header object at 0x0000015443AF6AC8>
    # print(f.offsets)
    # print(f.samples)   #[0.000e+00 1.000e+00 2.000e+00 ... 1.998e+03 1.999e+03 2.000e+03]
    # print(f.text)
    '''
    bytearray(b'C 1 SEGY OUTPUT FROM Petrel 2013.2 (64-bit) Wednesday, October 17 2018 12:37:30 
                C 2 Name: LX_mig2 \xd5Crop\xe5 1 Type: 3D seismic               
                  C 3                                                           
                  C 4 First inline: 730    Last inline: 1790                    
                  C 5 First xline:  200    Last xline:  440                     
                  C 6 CRS: Undefined                                            
                  C 7 X min: 472427.00 max: 477247.00 delta: 4820.00            
                  C 8 Y min: 4216434.00 max: 4237654.00 delta: 21220.00         
                  C 9 Time min: -2000.50 max: 0.50 delta: 2001.00               
                  C10 Lat min: - max: - delta: -                                
                  C11 Long min: - max: - delta: -                               
                  C12 Trace min: -2000.00 max: 0.00 delta: 2000.00              
                  C13 Seismic (template) min: ~-245391.69 max: ~208256.25 delta: ~453647.94       
                  C14 Amplitude (data) min: ~-245391.69 max: ~208256.25 delta: ~453647.94         
                  C15 Trace sample format: IBM floating point                   
                  C16 Coordinate scale factor: 1.00000                          
                  C17                                                           
                  C18 Binary header locations:                                  
                  C19 Sample interval             : bytes 17-18                 
                  C20 Number of samples per trace : bytes 21-22                 
                  C21 Trace date format           : bytes 25-26                 
                  C22                                                           
                  C23 Trace header locations:                                   
                  C24 Inline number               : bytes 5-8                   
                  C25 Xline number                : bytes 21-24                 
                  C26 Coordinate scale factor     : bytes 71-72                 
                  C27 X coordinate                : bytes 73-76                 
                  C28 Y coordinate                : bytes 77-80                 
                  C29 Trace start time/depth      : bytes 109-110               
                  C30 Number of samples per trace : bytes 115-116               
                  C31 Sample interval             : bytes 117-118               
                  C32                                                           
                  C33                                                           
                  C34                                                           
                  C35                                                           
                  C36                                                           
                  C37                                                           
                  C38                                                           
                  C39                                                           
                  C40 END EBCDIC                                                
    '''
    # print(f.trace)                                              # Trace(traces = 255701, samples = 2001)
    # print(f.tracecount)
    # print(f.unstructured)
    # print(f.xfd)
    # print(f.xlines)                                             # None
    # print(f.__delattr__)
    # print(f.trace[1][1])
    # print(f.trace[1][2])
    # print(f.trace[10000][700])                                  # -7994.883
    # print(f.trace[10000][701])                                  # -10279.133
    # print(f.trace[10000][2000])                                 # 18274.016
    # print(f.trace[10000][0])
    # print(f.trace[255700][0])
    # print(f.trace[0][0])
    # print(f.header[0][segyio.TraceField.GroupX])
    # print(f.header[20000][segyio.TraceField.GroupX])
    # print(f.header[200000][segyio.TraceField.GroupX])
    # print(f.header[20000][segyio.TraceField.GroupY])
    # print(f.bin[segyio.BinField.Samples] == f.samples)    # [False False False ... False False False]
    # print(segyio.TraceField.TRACE_SAMPLE_COUNT)           # 115
    # print(segyio.TraceField.TRACE_SEQUENCE_LINE)          # 1
    # print(f.header[0][1])                                 # 1
    # print(f.header[25570][1])                             # 25
    # print(f.header[25570*2][1])                           # 49
    # print(f.header[25570*3][1])                           # 73
    # print(segyio.TraceField.GroupX)                       # 81
    # print(segyio.TraceField.GroupY)                       # 85
    # print(f.header[0][segyio.TraceField.GroupX])          # 0
    # print(f.header[25570][segyio.TraceField.GroupX])      # 0
    # print(f.header[25570*2][segyio.TraceField.GroupX])    # 0
    # print(f.header[25570*3][segyio.TraceField.GroupX])    # 0
    # print(f.header[25570*4][segyio.TraceField.GroupX])    # 0
    # print(f.header[25570*5][segyio.TraceField.GroupX])    # 0
    # print(f.header[25570*6][segyio.TraceField.GroupX])    # 0
    # print(f.header[25570*7][segyio.TraceField.GroupX])    # 0
    # print(f.header[25570*4][segyio.TraceField.GroupY])    # 0
    # print(f.header[25570*5][segyio.TraceField.GroupY])    # 0
    # print(f.header[25570*6][segyio.TraceField.GroupY])    # 0
    # print(f.header[25570*7][segyio.TraceField.GroupY])    # 0
    # print(f.bin[segyio.BinField.Traces])                  # 1
    # print(f.tracecount)                                   # 255701(241*1061)
    # print( f.bin[segyio.BinField.Interval])               # 1000
    # print(f.bin[segyio.BinField.Samples]   )              # 2001
    # print(f.bin[segyio.BinField.SortingCode])             # 4
    # print(f.bin[segyio.BinField.Format])                  # 1
    # print(f.bin[segyio.BinField.JobID])
    # print(f.bin[segyio.BinField.LineNumber])
    # print(f.bin[segyio.BinField.MeasurementSystem])
    # print(f.bin[segyio.BinField.SEGYRevision])
    # print(f.bin[segyio.BinField.Samples])
    # print(f.bin[segyio.BinField.SamplesOriginal])
    # print(f.bin[segyio.BinField.Traces])
    # print(segyio.su.xline)                                # 193
    # print(segyio.su.cdp)                                  # 21
    # print(segyio.su.gx)                                   # 81
    # print(segyio.tools.collect(f.trace[:]))
    '''
        [[     0.          0.          0.     ...  -7441.8984  -4465.1406
        -1488.3799]
        [     0.          0.          0.     ... -12644.5625 -10413.168
        -7437.9766]
        [     0.          0.          0.     ... -16771.691  -14908.168
        -13665.82  ]
        ...
        [     0.          0.          0.     ... -23460.285  -20527.75
        -17595.215 ]
        [     0.          0.          0.     ... -21433.207  -19902.266
        -16840.379 ]
        [     0.          0.          0.     ... -19742.281  -16705.008
        -13667.73  ]]
    '''
    # x = segyio.tools.collect(f.trace[:])
    # x = x.reshape((len(f.ilines), len(f.xlines), f.samples))
    # np.all(x == segyio.tools.cube(f))
    # print(f.trace[0])               # [     0.         0.         0.     ... -7441.8984 -4465.1406 -1488.3799]
    # print(f.trace[1])               # [     0.         0.         0.     ... -12644.5625 -10413.168 -7437.9766]
    # print(f.trace[255700])          # [     0.         0.         0.     ... -19742.281 -16705.008 -13667.73 ]
    # print( f.trace[-2])             # [     0.         0.         0.    ... -21433.207 -19902.266 -16840.379]
    # print(f.trace[15:45])           # <generator object Trace.__getitem__.<locals>.gen at 0x000001C15EC02B48>
    # print(f.trace[:45:3])           # <generator object Trace.__getitem__.<locals>.gen at 0x000001E2D2812648>
    # print(f.trace[255700][2000])    # -13667.73
    # print(f.xline[2])  # NoneType
    # print(f.header[189])
    # print(f.header[0])
    '''
    {TRACE_SEQUENCE_LINE: 1, TRACE_SEQUENCE_FILE: 730, FieldRecord: 730, TraceNumber: 1, 
    EnergySourcePoint: 0, CDP: 200, CDP_TRACE: 1, TraceIdentificationCode: 1, NSummedTraces: 0, 
    NStackedTraces: 0, DataUse: 1, offset: 0, ReceiverGroupElevation: 0, SourceSurfaceElevation: 0, 
    SourceDepth: 0, ReceiverDatumElevation: 0, SourceDatumElevation: 0, SourceWaterDepth: 0, 
    GroupWaterDepth: 0, ElevationScalar: 1, SourceGroupScalar: -100, SourceX: 47243700, 
    SourceY: 421644400, GroupX: 0, GroupY: 0, CoordinateUnits: 1, WeatheringVelocity: 0, 
    SubWeatheringVelocity: 0, SourceUpholeTime: 0, GroupUpholeTime: 0, SourceStaticCorrection: 0, 
    GroupStaticCorrection: 0, TotalStaticApplied: 0, LagTimeA: 0, LagTimeB: 0, DelayRecordingTime: 0, 
    MuteTimeStart: 0, MuteTimeEND: 0, TRACE_SAMPLE_COUNT: 2001, TRACE_SAMPLE_INTERVAL: 1000, GainType: 0, 
    InstrumentGainConstant: 0, InstrumentInitialGain: 0, Correlated: 1, SweepFrequencyStart: 0, 
    SweepFrequencyEnd: 0, SweepLength: 0, SweepType: 1, SweepTraceTaperLengthStart: 0, 
    SweepTraceTaperLengthEnd: 0, TaperType: 1, AliasFilterFrequency: 0, AliasFilterSlope: 0, 
    NotchFilterFrequency: 0, NotchFilterSlope: 0, LowCutFrequency: 0, HighCutFrequency: 0, 
    LowCutSlope: 0, HighCutSlope: 0, YearDataRecorded: 0, DayOfYear: 0, HourOfDay: 0, 
    MinuteOfHour: 0, SecondOfMinute: 0, TimeBaseCode: 1, TraceWeightingFactor: 0, GeophoneGroupNumberRoll1: 0, 
    GeophoneGroupNumberFirstTraceOrigField: 0, GeophoneGroupNumberLastTraceOrigField: 0, 
    GapSize: 0, OverTravel: 0, CDP_X: 47243700, CDP_Y: 421644400, INLINE_3D: 730, CROSSLINE_3D: 200, 
    ShotPoint: 0, ShotPointScalar: 0, TraceValueMeasurementUnit: 0, TransductionConstantMantissa: 0, 
    TransductionConstantPower: 0, TransductionUnit: 0, TraceIdentifier: 0, ScalarTraceHeader: 0, SourceType: 0, 
    SourceEnergyDirectionMantissa: 0, SourceEnergyDirectionExponent: 0, SourceMeasurementMantissa: 0, 
    SourceMeasurementExponent: 0, SourceMeasurementUnit: 0}
    '''
    # print({segyio.su.tracl: 10})                    # {1: 10}
    # print(f.header[5])
    # print(f.header[5].items())
    # print(f.header[5][25, 37])
    # print(f.header[5][189])               # 730          INLINE_3D
    # print(f.header[5][193])               # 205          CROSSLINE_3D
    # print(f.header[6][193])               # 206          CROSSLINE_3D
    # print(f.header[7][193])               # 207          CROSSLINE_3D
    ############################################################################
    '''
    for i in range(0, 255700, m.floor(255700/10)):
        id = f.header[i][segyio.TraceField.TRACE_SEQUENCE_LINE]     # TRACE_SEQUENCE_LINE= 1            0
        # x = f.header[i][segyio.TraceField.GroupX]                   # GroupX= 81                        0
        # y = f.header[i][segyio.TraceField.GroupY]                   # GroupY= 85                        0
        x = f.header[i][segyio.TraceField.INLINE_3D]
        y = f.header[i][segyio.TraceField.CROSSLINE_3D]
        print("  %8d%12.2f%12.2f" % (id, x, y))
        print("===========================================")
        mySeis = np.zeros((255, 200), dtype=np.float32)
        for i in range(255):
            for j in range(200):
                mySeis[i][j] = f.trace[i][j]
        # f.close()
                print(mySeis[i][j])
        # return (mySeis)
     '''
    #############################################################################
    '''
            1      730.00      200.00
        ===========================================
            25      836.00      224.00
        ===========================================
            49      942.00      248.00
        ===========================================
            73     1048.00      272.00
        ===========================================
            97     1154.00      296.00
        ===========================================
            121     1260.00      320.00
        ===========================================
            145     1366.00      344.00
        ===========================================
            169     1472.00      368.00
        ===========================================
            193     1578.00      392.00
        ===========================================
            217     1684.00      416.00
        ===========================================
    '''
    # print(f.xline[f.xlines[1]])             # strict=False
    '''
        [[     0.          0.          0.     ... -12644.5625 -10413.168
        -7437.9766]
        [     0.          0.          0.     ... -12894.371  -11604.934
        -9670.777 ]
        [     0.          0.          0.     ... -11844.582  -11221.184
        -10597.785 ]
        ...
        [     0.          0.          0.     ...  -6935.6914  -9247.586
        -10403.535 ]
        [     0.          0.          0.     ...  -6967.207   -9289.609
        -11612.012 ]
        [     0.          0.          0.     ...  -6999.133   -9332.176
        -10498.699 ]]
    '''
    # print(f.depth_slice[100])
    '''
        [[0. 0. 0. ... 0. 0. 0.]
        [0. 0. 0. ... 0. 0. 0.]
        [0. 0. 0. ... 0. 0. 0.]
        ...
        [0. 0. 0. ... 0. 0. 0.]
        [0. 0. 0. ... 0. 0. 0.]
        [0. 0. 0. ... 0. 0. 0.]]
    '''
    # print(segyio.tools.cube(filename))
    '''
        [[[     0.          0.          0.     ...  -7441.8984  -4465.1406
            -1488.3799]
        [     0.          0.          0.     ... -12644.5625 -10413.168
            -7437.9766]
        [     0.          0.          0.     ... -16771.691  -14908.168
        -13665.82  ]
        ...
        [     0.          0.          0.     ... -10249.512  -13976.605
        -18635.473 ]
        [     0.          0.          0.     ... -11399.273  -15199.031
        -18998.79  ]
        [     0.          0.          0.     ...  -9495.508  -11394.609
        -14243.262 ]]

        [[     0.          0.          0.     ...  -9189.324   -7351.461
            -5513.5938]
        [     0.          0.          0.     ... -12894.371  -11604.934
            -9670.777 ]
        [     0.          0.          0.     ... -15757.211  -15173.609
        -14590.012 ]
        ...
        [     0.          0.          0.     ... -11819.234  -16365.094
        -20001.781 ]
        [     0.          0.          0.     ... -15914.914  -18567.402
        -22104.05  ]
        [     0.          0.          0.     ... -13776.281  -16531.54
        -18368.379 ]]

        [[     0.          0.          0.     ...  -9589.844   -8990.477
            -8391.113 ]
        [     0.          0.          0.     ... -11844.582  -11221.184
        -10597.785 ]
        [     0.          0.          0.     ... -14414.641  -14414.641
        -13838.055 ]
        ...
        [     0.          0.          0.     ... -12322.895  -15843.719
        -18484.34  ]
        [     0.          0.          0.     ... -17688.543  -20215.477
        -21900.102 ]
        [     0.          0.          0.     ... -17489.695  -19238.664
        -20987.633 ]]

        ...

        [[     0.          0.          0.     ...  -6918.59    -9224.789
        -11530.984 ]
        [     0.          0.          0.     ...  -6935.6914  -9247.586
        -10403.535 ]
        [     0.          0.          0.     ...  -5861.039   -8205.453
        -10549.871 ]
        ...
        [     0.          0.          0.     ... -25652.375  -22802.11
        -18526.715 ]
        [     0.          0.          0.     ... -23734.45   -22251.047
        -19284.242 ]
        [     0.          0.          0.     ... -20561.305  -19092.637
        -17623.973 ]]

        [[     0.          0.          0.     ...  -8010.7305 -10299.508
        -11443.898 ]
        [     0.          0.          0.     ...  -6967.207   -9289.609
        -11612.012 ]
        [     0.          0.          0.     ...  -7138.8945  -8328.711
        -10708.344 ]
        ...
        [     0.          0.          0.     ... -24465.379  -21587.098
        -18708.816 ]
        [     0.          0.          0.     ... -22460.16   -20962.816
        -17968.129 ]
        [     0.          0.          0.     ... -20797.227  -19311.71
        -16340.68  ]]

        [[     0.          0.          0.     ...  -8031.0586 -10325.645
        -11472.9375]
        [     0.          0.          0.     ...  -6999.133   -9332.176
        -10498.699 ]
        [     0.          0.          0.     ...  -7210.1094  -8411.793
        -10815.16  ]
        ...
        [     0.          0.          0.     ... -23460.285  -20527.75
        -17595.215 ]
        [     0.          0.          0.     ... -21433.207  -19902.266
        -16840.379 ]
        [     0.          0.          0.     ... -19742.281  -16705.008
        -13667.73  ]]]
    '''
    # print(f.attributes(segyio.TraceField.SourceX)[:])              # [47243700 47245700 47247700 ... 47719700 47721700 47723700]
    # print(f.attributes(segyio.TraceField.SourceY)[:])              # [421644400 421644400 421644400 ... 423764400 423764400 423764400]
    # print(f.attributes(segyio.TraceField.NSummedTraces)[:])        # [0 0 0 ... 0 0 0]
    # print(f.attributes(segyio.TraceField.NStackedTraces)[:])       # [0 0 0 ... 0 0 0]
    '''
    f.mmap()

    # Extract header word for all traces
    sourceX = f.attributes(segyio.TraceField.SourceX)[:]

    # Scatter plot sources and receivers color-coded on their number
    plt.figure()
    sourceY = f.attributes(segyio.TraceField.SourceY)[:]
    nsum = f.attributes(segyio.TraceField.NSummedTraces)[:]
    plt.scatter(sourceX, sourceY, c=nsum, edgecolor='none')
    plt.show()
    '''
    # groupX = f.attributes(segyio.TraceField.GroupX)[:]
    # groupY = f.attributes(segyio.TraceField.GroupY)[:]
    # nstack = f.attributes(segyio.TraceField.NStackedTraces)[:]
    # plt.scatter(groupX, groupY, c=nstack, edgecolor='none')
    # plt.show()
    # print(f.attributes(segyio.TraceField.SourceY)[10])
    # print(segyio.BinField.Traces)
    # for i in range(0, 160801, m.floor(160801/10)):
    #     print(f.header[i][segyio.TraceField.TRACE_SEQUENCE_LINE])
    # print(segyio.TraceField.TRACE_SEQUENCE_LINE)
    # print(segyio.BinField.Traces)                               # 3213      每个道集的数据道数。叠前数据强制要求
    # print(f.bin[segyio.BinField.Traces])                        # 1
    print(f.header[2557][segyio.TraceField.TRACE_SEQUENCE_LINE]
          )                        # 1
