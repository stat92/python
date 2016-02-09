# Здесь проверяется время выполнения встроенной функции
import time
import sys

if sys.platform[:3] == 'win':
    timefunc = time.clock           # В Windows использовать time.clock 
else:
    timefunc = time.time 			# На некоторых платформах Unix дает 
                                    # лучшее разрешение

reps = 10000
repslist = range(reps)
 
def timer(func, *pargs, **kargs):
    start = timefunc()
    for i in repslist:
        ret = func(*pargs, **kargs)
    elapsed = timefunc() - start
    return (elapsed, ret) 

def forLoop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res
 
def listComp():
    return [abs(x) for x in repslist]
 
def mapCall():
    return list(map(abs, repslist))    # Вызов list необходим только в 3.0
 
def genExpr():
    return list(abs(x) for x in repslist) # Функция list вынуждает 
                                          # вернуть сразу все результаты
def genFunc():
	def gen():
		for x in repslist:
			yield abs(x)
	return list(gen())
 
print(sys.version)
for test in (forLoop, listComp, mapCall, genExpr, genFunc):
    elapsed, result = timer(test)
    print ('-' * 33)
    print ('%-9s: %.5f => [%s...%s]' %
            (test.__name__, elapsed, result[0], result[-1]))
