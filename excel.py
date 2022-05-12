import math

class _ExcelError(Exception):
    pass

def ABS(number):
    '''Absolute value of a number.'''
    try: cnumber = int(number)
    except: raise TypeError('Only integers are allowed')
    return abs(cnumber)

def _ACCRINT_a(i):
    # number of accrued days for the quasi-coupon period within the odd period
    return 1

def _ACCRINT_nl(i):
    # normal length in days of the quasi-coupon period within the odd period
    return 1

def ACCRINT(issue, first_interest, settlement, rate, par, frequency, basis=0, calc_method=True):
    '''Accrued interest of security with periodic payments.'''
    if frequency not in [1, 2, 4]: raise _ExcelError('Incorrect frequency value, must be: 1, 2 or 4')
    nc = 1 # number of quasi-coupon periods that fit in the odd period
    sum_value = sum([(_ACCRINT_a(i) / _ACCRINT_nl(i)) for i in range(1, nc+1)])
    return par * (rate / frequency) * sum_value
    
def ACCRINTM(issue, settlement, rate, par, basis=0):
    '''Accrued interest of security paying at maturity.'''
    pass

def ACOS(number):
    '''Inverse cosine of a value, in radians.'''
    try: cnumber = float(number)
    except ValueError: raise _ExcelError('Only floats are allowed')
    return math.acos(cnumber)

def ACOSH(number):
    '''Inverse hyperbolic cosine of a number.'''
    try: cnumber = float(number)
    except ValueError: raise _ExcelError('Only floats are allowed')
    if cnumber < 1: raise _ExcelError(f'Value should be greater than or equal to 1.')
    return math.acosh(cnumber)

def ACOT():
    pass

def ACOTH():
    pass

def AGGREGATE():
    pass

def ADDRESS():
    pass

def AMORDEGRC():
    pass

def AMORLINC():
    pass

def AND(value, *values):
    pass

ARABIC_DICT = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

def ARABIC(text):
    parsed_text = str(text).strip().upper()
    if any(chr not in ARABIC_DICT.keys() for chr in parsed_text):
        raise TypeError('Input is not valid Roman numerals')
    if len(parsed_text) == 0: return 0
    result = 0
    for i,c in enumerate(parsed_text):
        if (i+1) == len(parsed_text) or ARABIC_DICT[c] >= ARABIC_DICT[parsed_text[i+1]]:
            result += ARABIC_DICT[c]
        else:
            result -= ARABIC_DICT[c]
    return result

def AREAS():
    pass

def ARRAYTOTEXT():
    pass

def ASC():
    pass

def ASIN():
    pass

def ASINH():
    pass

def ATAN():
    pass

def ATAN2():
    pass

def ATANH():
    pass

def AVEDEV():
    pass

def AVERAGE():
    pass

def AVERAGEA():
    pass

def AVERAGEIF():
    pass

def AVERAGEIFS():
    pass

def BAHTTEXT():
    pass

def BASE():
    pass

def BESSELI():
    pass

def BESSELJ():
    pass

def BESSELK():
    pass

def BESSELY():
    pass

def BETADIST():
    pass

def BETA_DIST():
    pass

def BETAINV():
    pass

def BETA_INV():
    pass

def BIN2DEC():
    pass

def BIN2HEX():
    pass

def BIN2OCT():
    pass

def BINOMDIST():
    pass

def BINOM_DIST():
    pass

def BINOM_DIST_RANGE():
    pass

def BINOM_INV():
    pass

def BITAND():
    pass

def BITLSHIFT():
    pass

def BITOR():
    pass

def BITRSHIFT():
    pass

def BITXOR():
    pass

def CALL():
    pass

def CEILING():
    pass

def CEILING_MATH():
    pass

def CEILING_PRECISE():
    pass

def CELL():
    pass

def CHAR():
    pass

def CHIDIST():
    pass

def CHIINV():
    pass

def CHITEST():
    pass

def CHISQ_DIST():
    pass

def CHISQ_DIST_RT():
    pass

def CHISQ_INV():
    pass

def CHISQ_INV_RT():
    pass

def CHISQ_TEST():
    pass

def CHOOSE():
    pass

def CLEAN():
    pass

def CODE():
    pass

def COLUMN():
    pass

def COLUMNS():
    pass

def COMBIN():
    pass

def COMBINA():
    pass

def COMPLEX():
    pass

def CONCAT():
    pass

def CONCATENATE():
    pass

def CONFIDENCE():
    pass

def CONFIDENCE_NORM():
    pass

def CONFIDENCE_T():
    pass

def CONVERT():
    pass

def CORREL():
    pass

def COS():
    pass

def COSH():
    pass

def COT():
    pass

def COTH():
    pass

def COUNT():
    pass

def COUNTA():
    pass

def COUNTBLANK():
    pass

def COUNTIF():
    pass

def COUNTIFS():
    pass

def COUPDAYBS():
    pass

def COUPDAYS():
    pass

def COUPDAYSNC():
    pass

def COUPNCD():
    pass

def COUPNUM():
    pass

def COUPPCD():
    pass

def COVAR():
    pass

def COVARIANCE_P():
    pass

def COVARIANCE_S():
    pass

def CRITBINOM():
    pass

def CSC():
    pass

def CSCH():
    pass

def CUBEKPIMEMBER():
    pass

def CUBEMEMBER():
    pass

def CUBEMEMBERPROPERTY():
    pass

def CUBERANKEDMEMBER():
    pass

def CUBESET():
    pass

def CUBESETCOUNT():
    pass

def CUBEVALUE():
    pass

def CUMIPMT():
    pass

def CUMPRINC():
    pass

def DATE():
    pass

def DATEDIF():
    pass

def DATEVALUE():
    pass

def DAVERAGE():
    pass

def DAY():
    pass

def DAYS():
    pass

def DAYS360():
    pass

def DB():
    pass

def DBCS():
    pass

def DCOUNT():
    pass

def DCOUNTA():
    pass

def DDB():
    pass

def DEC2BIN():
    pass

def DEC2HEX():
    pass

def DEC2OCT():
    pass

def DECIMAL():
    pass

def DEGREES():
    pass

def DELTA():
    pass

def DEVSQ():
    pass

def DGET():
    pass

def DISC():
    pass

def DMAX():
    pass

def DMIN():
    pass

def DOLLAR():
    pass

def DOLLARDE():
    pass

def DOLLARFR():
    pass

def DPRODUCT():
    pass

def DSTDEV():
    pass

def DSTDEVP():
    pass

def DSUM():
    pass

def DURATION():
    pass

def DVAR():
    pass

def DVARP():
    pass

def EDATE():
    pass

def EFFECT():
    pass

def ENCODEURL():
    pass

def EOMONTH():
    pass

def ERF():
    pass

def ERF_PRECISE():
    pass

def ERFC():
    pass

def ERFC_PRECISE():
    pass

def ERROR_TYPE():
    pass

def EUROCONVERT():
    pass

def EVEN():
    pass

def EXACT():
    pass

def EXP():
    pass

def EXPON_DIST():
    pass

def EXPONDIST():
    pass

def FACT():
    pass

def FACTDOUBLE():
    pass

def FALSE():
    pass

def F_DIST():
    pass

def FDIST():
    pass

def F_DIST_RT():
    pass

def FILTER():
    pass

def FILTERXML():
    pass

def FIND():
    pass

def FINDB():
    pass

def F_INV():
    pass

def F_INV_RT():
    pass

def FINV():
    pass

def FISHER():
    pass

def FISHERINV():
    pass

def FIXED():
    pass

def FLOOR():
    pass

def FLOOR_MATH():
    pass

def FLOOR_PRECISE():
    pass

def FORECAST():
    pass

def FORECAST_ETS():
    pass

def FORECAST_ETS_CONFINT():
    pass

def FORECAST_ETS_SEASONALITY():
    pass

def FORECAST_ETS_STAT():
    pass

def FORECAST_LINEAR():
    pass

def FORMULATEXT():
    pass

def FREQUENCY():
    pass

def F_TEST():
    pass

def FTEST():
    pass

def FV():
    pass

def FVSCHEDULE():
    pass

def GAMMA():
    pass

def GAMMA_DIST():
    pass

def GAMMADIST():
    pass

def GAMMA_INV():
    pass

def GAMMAINV():
    pass

def GAMMALN():
    pass

def GAMMALN_PRECISE():
    pass

def GAUSS():
    pass

def GCD():
    pass

def GEOMEAN():
    pass

def GESTEP():
    pass

def GETPIVOTDATA():
    pass

def GROWTH():
    pass

def HARMEAN():
    pass

def HEX2BIN():
    pass

def HEX2DEC():
    pass

def HEX2OCT():
    pass

def HLOOKUP():
    pass

def HOUR():
    pass

def HYPERLINK():
    pass

def HYPGEOM_DIST():
    pass

def HYPGEOMDIST():
    pass

def IF():
    pass

def IFERROR():
    pass

def IFNA():
    pass

def IFS():
    pass

def IMABS():
    pass

def IMAGINARY():
    pass

def IMARGUMENT():
    pass

def IMCONJUGATE():
    pass

def IMCOS():
    pass

def IMCOSH():
    pass

def IMCOT():
    pass

def IMCSC():
    pass

def IMCSCH():
    pass

def IMDIV():
    pass

def IMEXP():
    pass

def IMLN():
    pass

def IMLOG10():
    pass

def IMLOG2():
    pass

def IMPOWER():
    pass

def IMPRODUCT():
    pass

def IMREAL():
    pass

def IMSEC():
    pass

def IMSECH():
    pass

def IMSIN():
    pass

def IMSINH():
    pass

def IMSQRT():
    pass

def IMSUB():
    pass

def IMSUM():
    pass

def IMTAN():
    pass

def INDEX():
    pass

def INDIRECT():
    pass

def INFO():
    pass

def INT():
    pass

def INTERCEPT():
    pass

def INTRATE():
    pass

def IPMT():
    pass

def IRR():
    pass

def ISBLANK():
    pass

def ISERR():
    pass

def ISERROR():
    pass

def ISEVEN():
    pass

def ISFORMULA():
    pass

def ISLOGICAL():
    pass

def ISNA():
    pass

def ISNONTEXT():
    pass

def ISNUMBER():
    pass

def ISODD():
    pass

def ISREF():
    pass

def ISTEXT():
    pass

def ISO_CEILING():
    pass

def ISOWEEKNUM():
    pass

def ISPMT():
    pass

def JIS():
    pass

def KURT():
    pass

def LARGE():
    pass

def LCM():
    pass

def LEFT():
    pass

def LEFTB():
    pass

def LEN():
    pass

def LENB():
    pass

def LET():
    pass

def LINEST():
    pass

def LN():
    pass

def LOG():
    pass

def LOG10():
    pass

def LOGEST():
    pass

def LOGINV():
    pass

def LOGNORM_DIST():
    pass

def LOGNORMDIST():
    pass

def LOGNORM_INV():
    pass

def LOOKUP():
    pass

def LOWER():
    pass

def MATCH():
    pass

def MAX():
    pass

def MAXA():
    pass

def MAXIFS():
    pass

def MDETERM():
    pass

def MDURATION():
    pass

def MEDIAN():
    pass

def MID():
    pass

def MIDB():
    pass

def MIN():
    pass

def MINIFS():
    pass

def MINA():
    pass

def MINUTE():
    pass

def MINVERSE():
    pass

def MIRR():
    pass

def MMULT():
    pass

def MOD():
    pass

def MODE():
    pass

def MODE_MULT():
    pass

def MODE_SNGL():
    pass

def MONTH():
    pass

def MROUND():
    pass

def MULTINOMIAL():
    pass

def MUNIT():
    pass

def N():
    pass

def NA():
    pass

def NEGBINOM_DIST():
    pass

def NEGBINOMDIST():
    pass

def NETWORKDAYS():
    pass

def NETWORKDAYS_INTL():
    pass

def NOMINAL():
    pass

def NORM_DIST():
    pass

def NORMDIST():
    pass

def NORMINV():
    pass

def NORM_INV():
    pass

def NORM_S_DIST():
    pass

def NORMSDIST():
    pass

def NORM_S_INV():
    pass

def NORMSINV():
    pass

def NOT():
    pass

def NOW():
    pass

def NPER():
    pass

def NPV():
    pass

def NUMBERVALUE():
    pass

def OCT2BIN():
    pass

def OCT2DEC():
    pass

def OCT2HEX():
    pass

def ODD():
    pass

def ODDFPRICE():
    pass

def ODDFYIELD():
    pass

def ODDLPRICE():
    pass

def ODDLYIELD():
    pass

def OFFSET():
    pass

def OR():
    pass

def PDURATION():
    pass

def PEARSON():
    pass

def PERCENTILE_EXC():
    pass

def PERCENTILE_INC():
    pass

def PERCENTILE():
    pass

def PERCENTRANK_EXC():
    pass

def PERCENTRANK_INC():
    pass

def PERCENTRANK():
    pass

def PERMUT():
    pass

def PERMUTATIONA():
    pass

def PHI():
    pass

def PHONETIC():
    pass

def PI():
    pass

def PMT():
    pass

def POISSON_DIST():
    pass

def POISSON():
    pass

def POWER():
    pass

def PPMT():
    pass

def PRICE():
    pass

def PRICEDISC():
    pass

def PRICEMAT():
    pass

def PROB():
    pass

def PRODUCT():
    pass

def PROPER():
    pass

def PV():
    pass

def QUARTILE():
    pass

def QUARTILE_EXC():
    pass

def QUARTILE_INC():
    pass

def QUOTIENT():
    pass

def RADIANS():
    pass

def RAND():
    pass

def RANDARRAY():
    pass

def RANDBETWEEN():
    pass

def RANK_AVG():
    pass

def RANK_EQ():
    pass

def RANK():
    pass

def RATE():
    pass

def RECEIVED():
    pass

def REGISTER_ID():
    pass

def REPLACE():
    pass

def REPLACEB():
    pass

def REPT():
    pass

def RIGHT():
    pass

def RIGHTB():
    pass

def ROMAN():
    pass

def ROUND():
    pass

def ROUNDDOWN():
    pass

def ROUNDUP():
    pass

def ROW():
    pass

def ROWS():
    pass

def RRI():
    pass

def RSQ():
    pass

def RTD():
    pass

def SEARCH():
    pass

def SEARCHB():
    pass

def SEC():
    pass

def SECH():
    pass

def SECOND():
    pass

def SEQUENCE():
    pass

def SERIESSUM():
    pass

def SHEET():
    pass

def SHEETS():
    pass

def SIGN():
    pass

def SIN():
    pass

def SINH():
    pass

def SKEW():
    pass

def SKEW_P():
    pass

def SLN():
    pass

def SLOPE():
    pass

def SMALL():
    pass

def SORT():
    pass

def SORTBY():
    pass

def SQRT():
    pass

def SQRTPI():
    pass

def STANDARDIZE():
    pass

def STOCKHISTORY():
    pass

def STDEV():
    pass

def STDEV_P():
    pass

def STDEV_S():
    pass

def STDEVA():
    pass

def STDEVP():
    pass

def STDEVPA():
    pass

def STEYX():
    pass

def SUBSTITUTE():
    pass

def SUBTOTAL():
    pass

def SUM():
    pass

def SUMIF():
    pass

def SUMIFS():
    pass

def SUMPRODUCT():
    pass

def SUMSQ():
    pass

def SUMX2MY2():
    pass

def SUMX2PY2():
    pass

def SUMXMY2():
    pass

def SWITCH():
    pass

def SYD():
    pass

def T():
    pass

def TAN():
    pass

def TANH():
    pass

def TBILLEQ():
    pass

def TBILLPRICE():
    pass

def TBILLYIELD():
    pass

def T_DIST():
    pass

def T_DIST_2T():
    pass

def T_DIST_RT():
    pass

def TDIST():
    pass

def TEXT():
    pass

def TEXTJOIN():
    pass

def TIME():
    pass

def TIMEVALUE():
    pass

def T_INV():
    pass

def T_INV_2T():
    pass

def TINV():
    pass

def TODAY():
    pass

def TRANSPOSE():
    pass

def TREND():
    pass

def TRIM():
    pass

def TRIMMEAN():
    pass

def TRUE():
    pass

def TRUNC():
    pass

def T_TEST():
    pass

def TTEST():
    pass

def TYPE():
    pass

def UNICHAR():
    pass

def UNICODE():
    pass

def UNIQUE():
    pass

def UPPER():
    pass

def VALUE():
    pass

def VALUETOTEXT():
    pass

def VAR():
    pass

def VAR_P():
    pass

def VAR_S():
    pass

def VARA():
    pass

def VARP():
    pass

def VARPA():
    pass

def VDB():
    pass

def VLOOKUP():
    pass

def WEBSERVICE():
    pass

def WEEKDAY():
    pass

def WEEKNUM():
    pass

def WEIBULL():
    pass

def WEIBULL_DIST():
    pass

def WORKDAY():
    pass

def WORKDAY_INTL():
    pass

def XIRR():
    pass

def XLOOKUP():
    pass

def XMATCH():
    pass

def XNPV():
    pass

def XOR():
    pass

def YEAR():
    pass

def YEARFRAC():
    pass

def YIELD():
    pass

def YIELDDISC():
    pass

def YIELDMAT():
    pass

def Z_TEST():
    pass

def ZTEST():
    pass