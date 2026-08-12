RECOMMENDATIONS={
"happy":[("Good 4 U","Olivia Rodrigo"),("Levitating","Dua Lipa"),("Walking on Sunshine","Katrina & The Waves")],
"sad":[("Lovely","Billie Eilish"),("Someone You Loved","Lewis Capaldi"),("The Night We Met","Lord Huron")],
"angry":[("Believer","Imagine Dragons"),("Centuries","Fall Out Boy"),("Lose Yourself","Eminem")],
"fear":[("Weightless","Marconi Union"),("Experience","Ludovico Einaudi"),("Clair de Lune","Claude Debussy")],
"neutral":[("Sunflower","Post Malone"),("Sweater Weather","The Neighbourhood"),("Yellow","Coldplay")],
"surprise":[("Blinding Lights","The Weeknd"),("Don't Start Now","Dua Lipa"),("Electric Feel","MGMT")],
"disgust":[("Feel Good Inc.","Gorillaz"),("Take a Walk","Passion Pit"),("Seven Nation Army","The White Stripes")]
}
def recommend(expression):
    return [{"title":t,"artist":a} for t,a in RECOMMENDATIONS.get(expression,[])]
