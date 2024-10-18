import pandas as pd

d1 = {'A':[1,0,0,1], 'B':[0,1,1,0], 'C':[0,1,1,0], 'D':[1,0,0,1]}

# the prints are for testing output



# Problem 1
def makeDataFrame(data):
	# YOUR SOLUTION STARTS HERE
	df1 = pd.DataFrame(data)
	return df1
    # YOUR SOLUTION ENDS HERE

print(makeDataFrame(d1))




import pandas as pd
# Problem 2a
def load():
	#SOLUTION START( ~ 1 line of code)
	
	return pd.read_csv('data/openrice.csv',index_col=[0])
	#SOLUTION END


df = load() # use df for the remaining problems




# Problem 2b
def makeCategory():
	#SOLUTION START( ~ 1-2 lines of code)
	price_dict = {
	"Below $50" : 'Cheap',
	"$51-100" : 'Not Cheap',
	"$101-200": 'Expensive',
	"$201-400": 'Very Expensive'
	}

	df['price_category'] = df['price_range'].map(price_dict)
	return df['price_category']
	#SOLUTION END

print(makeCategory())





# Problem 2c
def totalDislike():
	#SOLUTION START( ~ 1-2 line of code)
	return df.groupby('price_range')['dislikes'].sum()
	#SOLUTION END

print(totalDislike())






# Problem 2d
def totalBookmarks():
	#SOLUTION START( ~ 1-2 line of code)
	return df[df['food_type']=='Hong Kong Style']['bookmarks'].sum()
	#SOLUTION END

print(totalBookmarks())





# Problem 2e
def extractReview():
	#SOLUTION START( ~ 1-2 line of code)
	df['number_of_reviews'] = df['number_of_reviews'].astype(str)
	df['number_of_reviews'] = df['number_of_reviews'].str.extract(r'(\d+)', expand=False).astype(int)
	return df['number_of_reviews'] 
	#SOLUTION END

print(extractReview())