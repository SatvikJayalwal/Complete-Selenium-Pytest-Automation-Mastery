# if/else, for loops, while loops, break, continue, pass

browser_name = "Chrome"
if browser_name=="Chrome" :
    print("Launching chrome...")

elif browser_name=="Firefox" :
    print("Launching firefox")

else:
    print("Nothing launched")

#Loops
nav_links = ["Home","About us","Contact","Careers"]
for link in nav_links:
    print(f"Clicking on the {link} link")

# While loops
loading_spinner_visible = True
seconds_waited = 0

while loading_spinner_visible:
    print(f"Waiting {seconds_waited}...seconds passed ")
    seconds_waited+=1
    if seconds_waited==3:
        loading_spinner_visible=False
        print("spinner_wheel disappeared")


# continue and break

shoe_brands = ["addidas","puma","nike","strava"]
for brand in shoe_brands:
    if brand=="puma":
        print("skipping puma...")
        continue

    print(f"checking {brand}")
    if brand=="nike":
        print("Found nike")
        break

#pass
while True:
    pass