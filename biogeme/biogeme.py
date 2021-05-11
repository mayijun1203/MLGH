import pandas as pd
import biogeme.biogeme
import biogeme.models


biogeme.version.getText()
pd.set_option('display.max_columns', None)

df=pd.read_csv('C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/biogeme/swissmetro.dat',sep='\t')

df.describe()

db=biogeme.database.Database('swissmetro',df)

db.getSampleSize()

globals().update(db.variables)

exclude=((PURPOSE!=1)*(PURPOSE!=3)+(CHOICE==0))>0

db.remove(exclude)


ASC_CAR=biogeme.expressions.Beta('ASC_CAR',0,None,None,0)
ASC_TRAIN=biogeme.expressions.Beta('ASC_TRAIN',0,None,None,0)
ASC_SM=biogeme.expressions.Beta('ASC_SM',0,None,None,1)
B_TIME=biogeme.expressions.Beta('B_TIME',0,None,None,0)
B_COST=biogeme.expressions.Beta('B_COST',0,None,None,0)



SM_COST=SM_CO*(GA==0)
TRAIN_COST=TRAIN_CO*(GA==0)
CAR_AV_SP = CAR_AV * (SP != 0)
TRAIN_AV_SP = TRAIN_AV * (SP != 0)
TRAIN_TT_SCALED = TRAIN_TT / 100.0
TRAIN_COST_SCALED = TRAIN_COST / 100
SM_TT_SCALED = SM_TT / 100.0
SM_COST_SCALED = SM_COST / 100
CAR_TT_SCALED = CAR_TT / 100
CAR_CO_SCALED = CAR_CO / 100




V1 = ASC_TRAIN +  B_TIME * TRAIN_TT_SCALED + B_COST * TRAIN_COST_SCALED
V2 = ASC_SM + \
     B_TIME * SM_TT_SCALED + \
     B_COST * SM_COST_SCALED
V3 = ASC_CAR + \
     B_TIME * CAR_TT_SCALED + \
     B_COST * CAR_CO_SCALED


V = {1: V1,
     2: V2,
     3: V3}

av = {1: TRAIN_AV_SP,
      2: SM_AV,
      3: CAR_AV_SP}




logprob = biogeme.models.loglogit(V, av, CHOICE)


bio = biogeme.biogeme.BIOGEME(db, logprob)
bio.modelName = 'swissmetro'

results = bio.estimate()


pandasResults = results.getEstimatedParameters()
print(pandasResults)

print(results)
results.writeHtml('C:/Users/mayij/Desktop/DOC/GITHUB/MLGH/biogeme/swissmetro.html')


