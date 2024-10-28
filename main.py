# Thayer Yang
# 28 OCT 2024
# Lists Stats

# QUIZ SCORES

quiz_scores = [88,77,64,53,92,41]

average = sum(quiz_scores)/len(quiz_scores)
print(f'The average score is {average:.2f}')

print()

# Driving Distances

locations, distances = ['Mount Pleasant', 'Grand Rapids', 'Williamsburg', 'Ann Arbor', 'Lansing'], [112.4, 142.0, 12.3,240.1,181.9 ]

longest_trip = max(distances)
longest_index = distances.index(longest_trip)
farthest_location = locations[longest_index]

shortest_trip = min(distances)
shortest_index = distances.index(shortest_trip)
closest_trip = locations[shortest_index]

print(f'The shortest trip from Traverse City Michigan is {closest_trip} with {shortest_trip} miles. With a round trip of {shortest_trip*2} miles')
print(f'The longest trip from Traverse City Michigan is {farthest_location} with {longest_trip} miles. With a round trip of {longest_trip*2} miles')

print()

for location in locations:
    index = locations.index(location)
    distance = distances[index]

    print(f'Traverse City to {location} has a {distance*2} mile round trip.')