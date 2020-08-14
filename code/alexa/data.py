# -*- coding: utf-8 -*-

# Resolving gettext as _ for module loading.
from gettext import gettext as _

SKILL_NAME = "San Francisco Guide"

WELCOME = _("Hey Globetrotter!Welcome to San Francisco City Guide.")
HELP = _("Say about, to know more about the city, or say coffee, breakfast, lunch, or dinner, to hear about local restaurant suggestions, or say recommend an attraction, or say, go outside to know about tourist spots. ")
ABOUT = _("San Francisco is the cultural, commercial, and financial center of Northern California.A popular tourist destination,San Francisco is known for its cool summers, fog, steep rolling hills, eclectic mix of architecture, and landmarks, including the Golden Gate Bridge, Fisherman's Wharf, and its Chinatown district.")
STOP = _("Okay, see you next time!")
FALLBACK = _("The {} can't help you with that. It can help you learn about San Francisco if you say tell me about this place. What can I help you with?")
GENERIC_REPROMPT = _("What can I help you with?")

CITY_DATA = {
    "city": "San Francisco",
    "state": "CA",
    "postcode": "94102",
    "restaurants": [
        {
            "name": 'Quince',
            "address": '470 Pacific Ave, San Francisco, CA 94133',
            "phone": '(415) 775-8500',
            "meals": 'dinner',
            "description": 'Quince features Californian contemporary cuisine.It serves a nightly-changing tasting menu highlighting the restaurants unique partnership with Fresh Run Farm',
            "website":'quincerestaurant.com',
        },
        {
            "name": 'Lazy Bear',
            "address": '3416 19th St, San Francisco, CA 94110',
            "phone": '(415) 874-9921',
            "meals": 'dinner',
            "description": 'Each night Lazy Bear hosts a dinner party that is social, adventurous, and refined.',
            "website":'lazybearsf.com',
        },
        {
            "name": 'State Bird Provisions',
            "address": '1529 Fillmore St, San Francisco, CA 94115',
            "phone": '(415) 795-1272',
            "meals": 'lunch, dinner',
            "description": 'An adventurous, inventive, delicious, thoughtful contemporary American restaurant',
            "website":'statebirdsf.com',

        },
        {
            "name": 'Mourad',
            "address": '140 New Montgomery St #1, San Francisco, CA 94105',
            "phone": '(415) 660-2500',
            "meals": 'lunch, dinner',
            "description":'Upscale Moroccan eatery in a glam space',
            "website": 'mouradsf.com',
        },
        {
            "name": 'House Of Prime Rib',
            "address": '1906 Van Ness Ave, San Francisco, CA 94109',
            "phone": '(415) 885-4605',
            "meals": 'dinner',
            "description": 'Serve only the best beef available, the top 2% of all beef marketed',
            "website":'houseofprimerib.net',
        },
        {
            "name": 'Octavia',
            "address": '178 Washington Street, San Francisco, CA 94111',
            "phone": '(415) 408-7507',
            "meals": 'dinner',
            "description": 'Refined yet casual New American bistro',
            "website":'octavia-sf.com',
        },
         {
            "name": 'Swan Oyster Depot',
            "address": '1517 Polk St, San Francisco, CA 94109',
            "phone": '(415) 673-1101',
            "meals": 'breakfast, lunch',
            "description": 'Venerable seafood bar in a fish market',
            "website":'swanoysterdepot.us',
        },
        {
            "name": 'Kusakabe',
            "address": '584 Washington St, San Francisco, CA 94111',
            "phone": '(415) 757-0155',
            "meals": 'dinner',
            "description": 'A destination for premium sushi featuring beautiful cuts of fish prepared with a precision that is inspiring to watch',
            "website":'kusakabe-sf.com',
        },
        {
            "name": 'B.Patisserie',
            "address": '2821 California St, San Francisco, CA 94115',
            "phone": '(415) 440-1700',
            "meals": 'coffee',
            "description": 'The space sports an appealing European feel, and while the line can be daunting, dessert addicts pretty much can not go wrong.',
            "website":'bpatisserie.com',
        },
        {
            "name": 'The House',
            "address": '1230 Grant Ave, San Francisco, CA 94133',
            "phone": '(415) 986-8612',
            "meals": 'lunch, dinner',
            "description": 'Some of the citys top Asian-fusion fare can surprisingly be found in North Beach at this small but mighty good, eclectic place',
            "website":'thehse.com',
        },
        {
            "name": 'Zuni Cafe',
            "address": '1658 Market St, San Francisco, CA 94102',
            "phone": '(415) 552-2522',
            "meals": 'breakfast, lunch, dinner',
            "description": 'Incredibly well-executed menu of delectable, locally, sustainably sourced seasonal dishes with expertly mixed cocktails and pro service.',
            "website": 'zunicafe.com',
        },
        {
            "name": 'Delfina',
            "address": '3621 18th St, San Francisco, CA 94110',
            "phone": '(415) 552-4055',
            "meals": 'dinner',
            "description": 'This Mission mainstay has Northern Italian staples done superbly well, notably fantastic homemade pastas that just melt in your mouth',
            "website": 'delfinasf.com'
        },
        {
            "name": 'Plaj Restaurant',
            "address": '333 Fulton St, San Francisco, CA 94102',
            "phone": '(415) 294-8925',
            "meals": 'dinner',
            "description": 'Savory, modern Scandinavian fare and unusual, delicious cocktails provide a real taste treat at this quiet and cozy spot',
            "website":'plajrestaurant.com',
        },
         {
            "name": 'Mozzeria',
            "address": '3228 16th St, San Francisco, CA 94103',
            "phone": '(415) 489-0963',
            "meals": 'dinner',
            "description": 'The wood-fired pizza is wonderful with unique, engaging service by differently abled staff.',
            "website":'mozzeria.com',
        },
        {
            "name": 'Kiss Seafood',
            "address": '1700 Laguna St, San Francisco, CA 94115',
            "phone": '(415) 474-2866',
            "meals": 'dinner',
            "description": 'When it comes to amazing sushi and other superb Japanese dishes, this high-end Japantown eating joint provides an exemplary experience.',
            "website":'kissseafoodsf.com',
        },
        {
            "name": 'Harris, the San Francisco Steakhouse',
            "address": '2100 Van Ness Ave, San Francisco, CA 94109',
            "phone": '(415) 673-1888',
            "meals": 'lunch, dinner',
            "description": 'Steakhouses don’t get much more old-world than Harris where the chops are serious, the tabs are expensive and there’s mahogany everywhere; granted, as a throwback to another era',
            "website":'harrisrestaurant.com',
        },
        {
            "name": 'Nopa',
            "address": '560 Divisadero St, San Francisco, CA 94117',
            "phone": '(415) 864-8643',
            "meals": 'dinner',
            "description": 'Prices are decent, brunches are fantastic and its a favorite late-night spot',
            "website":'nopasf.com',
        },
        {
            "name": 'Piqueos',
            "address": '5631, 830 Cortland Ave, San Francisco, CA 94110',
            "phone": '(415) 282-8812',
            "meals": 'lunch, dinner',
            "description": 'You can find amazing ceviche and other beautifully presented Peruvian dishes with a modern flair',
            "website": 'piqueos.com',
        },
        {
            "name": 'Piperade',
            "address": '1015 Battery St, San Francisco, CA 94111',
            "phone": '(415) 391-2555',
            "meals": 'lunch, dinner',
            "description": 'This North Beach eatery has been consistently lauded for its top-notch, creative dishes that are expertly prepared and full of flavor',
            "website": 'piperade.com',
        },
        {
            "name": 'The Slanted Door',
            "address": 'Ferry Building, 1 Ferry Building #3, San Francisco, CA 94111',
            "phone": '(415) 861-8032',
            "meals": 'coffee, lunch, dinner',
            "description": 'Outstanding array of contemporary Vietnamese dishes fashioned from local, sustainable ingredients and an interesting wine list',
            "website":'slanteddoor.com',
        },
        {
            "name": 'Yank Sing (Stevenson Street)',
            "address": '49 Stevenson St, San Francisco, CA 94105',
            "phone": '(415) 541-4949',
            "meals": 'lunch',
            "description": 'This place has some of the best dumplings around; despite weekend and lunchtime mobs, service is wicked fast',
            "website":'yanksing.com',
        },
        {
            "name": 'Perbacco',
            "address": '230 California St, San Francisco, CA 94111',
            "phone": '(415) 955-0663',
            "meals": 'lunch, dinner',
            "description": 'A high-end Italian bistro that will titillate your taste buds with seasonal Piedmontese dishes that marry tradition with innovation.',
            "website":'perbaccosf.com',
        },
        {
            "name": 'Alexanders Steakhouse',
            "address": '1713, 448 Brannan St, San Francisco, CA 94107',
            "phone": '(415) 495-1111',
            "meals": 'lunch, dinner',
            "description": 'This place you are sure to find beef that melts in your mouth and the signature hamachi shots are presented alongside fantastic wines.',
            "website":'alexanderssteakhouse.com',
        },
        {
            "name": 'Benu',
            "address": '22 Hawthorne St, San Francisco, CA 94105',
            "phone": '(415) 685-4860',
            "meals": 'dinner',
            "description": 'You’ll be overwhelmed by the creativity and imagination put into each breathtaking dish, which has an incredible blend of Asian and Californian flavors.',
            "website":'benusf.com',
        },
        {
            "name": 'Tonys Pizza Napoletana',
            "address": '570 Stockton St, San Francisco, CA 94133',
            "phone": '(415) 835-9888',
            "meals": 'lunch, dinner',
            "description":'Tonys offers a great variety of incredible pizzas including Neapolitan-style Sicilian Californian Roman even gluten-free.',
            "website": 'tonyspizzanapoletana.com',
        },
        {
            "name": 'ONE65 Bistro & Grill',
            "address": '165 O Farrell Street, San Francisco, 94102',
            "phone": '(415) 814-8888',
            "meals": 'coffee, breakfast, lunch',
            "description": 'ONE65 is a six-story French dining destination that includes a patisserie and cafe, bistro, bar and lounge, fine dining restaurant and private dining space.',
            "website": 'one65sf.com'
        },
        {
            "name": 'Nari',
            "address": '1625 Post Street, San Francisco, CA 94115',
            "phone": '(415) 868-6274',
            "meals": 'dinner',
            "description": 'A contemporary Thai restaurant infusing heritage recipes with a modern Californian sensibility.The menu features dishes like rich curries with lamb, pork belly and Cornish game hen.',
            "website":'narisf.com',
        },
         {
            "name": 'Liholiho Yacht Club',
            "address": '871 Sutter St, San Francisco, CA 94109',
            "phone": '(415) 440-5446',
            "meals": 'lunch',
            "description": 'A fun-loving lower Nob Hill restaurant.The menu features dishes like lobster in black bean sauce and marinated squid with watermelon.',
            "website":'liholihoyachtclub.com',
        },
        {
            "name": 'Campton Place',
            "address": '340 Stockton St, San Francisco, CA 94108',
            "phone": '(415) 781-5555',
            "meals": 'breakfast, lunch, dinner',
            "description": 'A flavorful fusion of South Indian and California cuisines. The resulting exotic, high-end Cal-Indian cuisine has earned Campton Place Michelin stars since 2011.',
            "website":'camptonplacesf.com',
        },
         {
            "name": 'Acquerello',
            "address": '1722 Sacramento Street, San Francisco, CA 94109',
            "phone": '(415) 567-5432',
            "meals": 'dinner',
            "description": 'A masterful Italian restaurant with decadent dishes served in Old World style.',
            "website":'acquerellosf.com',
        },
        {
            "name": 'Mahila',
            "address": '1355 Market Street, San Francisco, CA 94103',
            "phone": '(415) 660-2020',
            "meals": 'dinner',
            "description": 'The food elevates rustic home style and street food dishes into vibrant explosions of flavor, often gloriously accented with delicate microgreens.',
            "website":'azalinas.com',
        },
        {
            "name": 'Angler San Francisco',
            "address": '132 The Embarcadero, San Francisco, CA 94105',
            "phone": '(415) 872-9442',
            "meals": 'lunch, dinner',
            "description": 'A waterfront restaurant with delicacies from land-and-sea concocted by Saisons famed chef.',
            "website":'anglerrestaurants.com',
        },
        {
            "name": 'Aziza',
            "address": '5800 Geary Blvd, San Francisco, CA 94121',
            "phone": '(415) 795-1272',
            "meals": 'dinner',
            "description": 'The perfect marriage of Moroccan flavors with Northern California ingredients, turning out dishes that continue to surprise and delight.',
            "website":'aziza-sf.com',

        },
        {
            "name": 'El Buen Comer',
            "address": '3435 Mission St, San Francisco, CA 94110',
            "phone": '(415) 817-1542',
            "meals": 'lunch, dinner',
            "description": 'Authentic Mexico City cuisine served family style.Brunch is now available on Saturdays and Sundays.',
            "website": 'elbuencomersf.com',
        },
        {
            "name": 'Cala',
            "address": '149 Fell St, San Francisco, CA 94102',
            "phone": '(415) 660-7701',
            "meals": 'dinner',
            "description": 'An impressive marriage of Mexican flavors and fresh seafood created by famed Mexico City chef, Gabriela Cámara.',
            "website": 'calarestaurant.com',
        },
        {
            "name": 'Californios',
            "address": '3115 22nd St, San Francisco, CA 94110',
            "phone": '(415) 757-0994',
            "meals": 'dinner',
            "description": 'A stylish, Michelin-starred Mexican restaurant replete with decadent and surprising dishes.',
            "website":'californiossf.com',
        },
        {
            "name": 'Prairie',
            "address": '3431 19th St, San Francisco, CA 94110',
            "phone": '(415) 483-1112',
            "meals": 'dinner',
            "description": 'Italian and Asian flavors fuse to create masterful charbroiled and slow-cooked fare.Offers brunch only on Sundays',
            "website":'prairiesf.com',
        },
        {
            "name": 'Palette Tea House',
            "address": '900 N Point St, San Francisco, CA 94109',
            "phone": '(415) 347-8888',
            "meals": 'lunch, dinner',
            "description": 'The latest and greatest dim sum parlor is at Ghirardelli Square and features eye-popping, Instagram-ready dumplings and fresh seafood.',
            "website":'paletteteahouse.com',
        },
        {
            "name": 'Petit Crenn',
            "address": '609 Hayes St, San Francisco, CA 94102',
            "phone": '(415) 864-1744',
            "meals": 'coffee, breakfast, lunch, dinner',
            "description": 'Rustic French flavors served in a bright, simplified modern space.Its affordable 5-course tasting menu is rife with delicate shellfish and succulent fish.',
            "website":'petitcrenn.com',
        },
        {
            "name": 'The Progress',
            "address": '1525 Fillmore St, San Francisco, CA 94115',
            "phone": '(415) 673-1294',
            "meals": 'dinner',
            "description": 'A family-style feast of California-influenced world flavors served in a stylish, former theater in the Fillmore.',
            "website":'theprogress-sf.com',
        },
         {
            "name": 'Kin Khao',
            "address": '55 Cyril Magnin St, San Francisco, CA 94110',
            "phone": '(415) 362-7456',
            "meals": 'lunch, dinner',
            "description": 'The ambiance is colorful and informal at this Michelin-starred Thai restaurant, from the decor to the bold curries.',
            "website":'kinkhao.com',
        },
        {
            "name": 'Dear Inga',
            "address": '3560 18th St, San Francisco, CA 94110',
            "phone": '(415) 829-2125',
            "meals": 'lunch',
            "description": 'Dear Inga utilizes fermentation, smoking and live fire in dishes that range from smoked sturgeon and pickled mussels to farmer’s cheese and bratwurst',
            "website":'dearinga.com',
        },
        {
            "name": 'Ayala',
            "address": '386 Geary St, San Francisco, CA 94102-1802',
            "phone": '(415) 374-7971',
            "meals": 'dinner',
            "description": 'A flavor-forward California seafood hotel-restaurant with a killer raw bar.',
            "website":'ayalarestaurant.com',
        },
        {
            "name": 'Tartine Manufactory',
            "address": '595 Alabama St, San Francisco, CA 94110',
            "phone": '(415) 757-0007',
            "meals": 'coffee',
            "description": 'An incubator for the citys best food-and-drink artisans with a light and breezy atmosphere and a bakery rivaled only by the original Tartine.',
            "website": 'tartinemanufactory.com',
        },
        {
            "name": 'Gibson',
            "address": '111 Mason St, San Francisco, CA 94102-2713',
            "phone": '(415) 771-7709',
            "meals": 'dinner',
            "description": 'Whether you prefer the charcoal-grilled sourdough bread or clams cooked in hay, the menu holds one pleasure after another.',
            "website":'gibsonsf.com',
        },
        {
            "name": 'Cassava',
            "address": '3519 Balboa Street, San Francisco, CA 94121',
            "phone": '(415) 640-8990',
            "meals": 'lunch, dinner',
            "description": 'This is a community gathering place that just happens to have an out-of-this-world menu.',
            "website":'cassavasf.com',
        },
        {
            "name": 'Corridor',
            "address": '100 Van Ness Ave, San Francisco, CA 94102',
            "phone": '(415) 834-5684',
            "meals": 'coffe, breakfast, lunch, dinner',
            "description": 'Starting with full breakfast offerings, as well as LAMILL coffee in the morning, to full service lunch and dinner with a vibrant bar, Corridor is your go to spot for all occasions.',
            "website":'corridorsf.com',
        },
        {
            "name": 'In Situ',
            "address": '151 3rd St, San Francisco, CA 94103-3107',
            "phone": '(415) 941-6050',
            "meals": 'lunch, dinner',
            "description": 'An innovative, Michelin-starred museum restaurant with contributions from world-class chefs from around the globe.',
            "website":'insitu.sfmoma.org',
        },
        {
            "name": 'Ju-Ni',
            "address": '1335 Fulton Street, San Francisco, CA 94117',
            "phone": '(415) 655-9924',
            "meals": 'lunch, dinner',
            "description": 'A tiny Japanese restaurant with an 18-course omakase menu sourced straight from Tokyo.',
            "website":'junisf.com',
        },
        {
            "name": 'La Taqueria',
            "address": '2889 Mission St, San Francisco, CA 94110',
            "phone": '(415) 285-7117',
            "meals": 'breakfast, lunch, dinner',
            "description": 'Home of the original Mission-style burrito, still a giant in a neighborhood now filled with dozens of imitators.',
            "website":'taqueriasanfrancisco.com',
        },
    ],
    "attractions": [
        {
            "name": 'Golden Gate Bridge',
            "description": 'The Golden Gate Bridge is a California icon gracing San Francisco Bay. It is the most photographed site in the city, with the orange structure backed by blue water, or in many cases, peaking through low lying cloud. At night, the flood-lit structure is equally striking.Use US Hwy 101, or SR 1 to drive over the bridge, and walkways on either side of the bridge are open to pedestrians and cyclists.',
            "distance":'0',
        },
        {
            "name": 'Alcatraz Island',
            "description": 'The historic and notorious Alcatraz penitentiary, located on Alcatraz Island, is one of Americas most infamous prisons.You can take a ferry over to the island and tour the site while listening to an exceptional audio recording that offers a glimpse into life in the prison.',
            "distance":'4',
        },
        {
            "name": 'Fishermans Wharf',
            "description": 'Fishermans Wharf, once the Little Italy of San Francisco, is known for its shops, restaurants, and beautiful setting along the waterfront.From here, you can take a sightseeing cruise, or organize a fishing charter.Some of the main attractions in the area are Madame Tussauds Wax Museum, Musée Mécanique, Ripleys Believe it or Not, and Ghirardelli Square.',
            "distance":'3',
        },
        {
            "name": 'Ride the Cable Cars',
            "description": 'Cable Cars, offer tourists a great way to explore the city in historic fashion.The Powell-Mason and Powell-Hyde are the most scenic routes.You can also get to Fisherman Wharf, Ghirardelli Square, the Ferry Building, Nob Hill, and Lombard Street through cable cars.',
            "distance":'6',
        },
        {
            "name": 'Golden Gate Park',
            "description": 'Golden Gate Park, home to gardens and museums, has more than 5,000 different kinds of plants and species of trees. The main attractions include the de Young Museum, the California Academy of Sciences Museum, the Japanese Tea Garden, and the San Francisco Botanical Garden. Bike rentals are available, which is a good way to explore the park.Alternatively, try an organized Segway Tour with a local guide.',
            "distance":'12',
        },
        {
            "name": 'Chinatown',
            "description": 'With its temples, theaters, antique and souvenir shops, and teahouses, Chinatown has become one of the major sites of San Francisco.The main street in Chinatown for tourists is Grant Avenue and Bush Street. You can do your own walking tour beginning in Chinatown.',
            "distance":'2',
        },
        {
            "name": 'Legion of Honor',
            "description": 'The California Palace of the Legion of Honor is San Franciscos most exquisite museum.It has a superb collection of European decorative arts, sculpture, and paintings, along with antiquities from the Mediterranean and Near East.',
            "distance":'5',
        },
        {
            "name": 'Palace of Fine Arts',
            "description": 'Listed on the National Register of Historic Places, this classical looking building is beautifully situated on a lagoon that reflects the mirror image on the surface of the calm water, while ducks and geese drift by.',
            "distance":'10',
        },
        {
            "name": 'California Academy of Sciences',
            "description": 'This state-of-the-art green building has an aqurium, rainforest and a museum inside.The Steinhart Aquarium includes 38,000 live specimens and a 25-feet-deep coral reef. The Osher Rainforest houses animals and amphibians.The Kimball Museum has skeletons of a T-Rex and blue whale, along with other interesting exhibits.',
            "distance":'9',
        },
        {
            "name": 'San Francisco Museum of Modern Art',
            "description": 'The San Francisco Museum of Modern Art has thousands of pieces and features an ever-changing selection of exhibitions.The museum is free for visitors 18 and younger.',
            "distance":'8',
        },
        {
            "name": 'de Young Fine Arts Museum of San Francisco',
            "description": 'In Golden Gate Park, the de Young Museum is a fine arts museum, and the exhibits cover a variety of time frames and geographical locations such as North America,Egypt, Greece, Rome, Africa, and the Pacific Islands.',
            "distance":'7',
        },
        {
            "name": 'Twin Peaks',
            "description": 'These two unique and uninhabited hills are more than 900 feet high.They have one of the finest views out over the city and bay and they are easy to access.You can drive to the north peak parking area for fine views and hike along trails over the north and south peaks.',
            "distance":'5',
        },
        {
            "name": 'Asian Art Museum',
            "description": 'The Asian Art Museum is one of the most important museums in San Francisco.It contains an extensive collection of sculptures, paintings, ceramics, jade carvings, and architectural fragments from Japan, Korea, China, India, Iran, and other Asiatic cultures.',
            "distance":'1',
        },
        {
            "name": 'Exploratorium',
            "description": 'One of San Franciscos top family attractions, the Exploratorium has exhibits for both children and adults.Children tend to rate this museum very highly, with all kinds of experiments and fun things to do, and most adults rave about the Exploratorium too.',
            "distance":'11',
        },
        {
            "name": 'High Tea at a Historic Hotel',
            "description": 'Enjoying high tea at a historic hotel gives tourists a sense of the citys grandeur during the Victorian era. The Fairmont San Francisco on Nob Hill, the Ritz-Carlton and the Palace Hotel awe visitors with their magnificent view and their tea servings.',
            "distance":'12',
        },
        {
            "name": 'Golden Gate National Recreation Area',
            "description": 'Golden Gate National Recreation Area, not to be confused with Golden Gate Park, is located across the Golden Gate Bridge from downtown San Francisco. This 600-square-mile park in Marin County is a designated Biosphere Reserve and  has walking trails, campgrounds, picnic areas, and beautiful beach areas',
            "distance":'13',
        },
        {
            "name": 'AT&T Park',
            "description": 'Home of the San Francisco Giants, AT&T park is a fun place to take in a baseball game while visiting the city. If you arent able to see a game, consider taking a ballpark tour.Tours are scheduled around games and do not run every day so check the online calendar in advance',
            "distance":'14',
        },
        {
            "name": 'Napa Valley',
            "description": 'Less than 1.5 hours from San Francisco, Napa Valley and Sonoma Valley are the two best-known and largest grape-growing areas in California. Many people day trip to this area to enjoy the scenery and stop in at some of the sites along the way.',
            "distance":'15',
        },
        {
            "name": 'Angel Island State Park',
            "description": 'If you are looking for a non-touristy thing to do in San Francisco, take a 25-minute ferry ride from Pier 41 to Angel Island State Park.You can enjoy the lovely scenery while hiking or biking on the well-groomed trails.The island also has five picnic areas, eleven campsites, and several sandy beaches.It also has a café that is open all week long and features live music performances.',
            "distance":'16',
        },
        {
            "name": 'Ghirardelli Square',
            "description": 'Located in the Fisherman Wharf area, Ghirardellis old red-brick chocolate factory has been turned into a center for shoppers, art-lovers, and those in search of entertainment or a good meal. This is a great place for chocolate lovers who want to sample some treats.',
            "distance":'17',
        },
        {
            "name": 'Pier 39',
            "description": 'Put Pier 39 on your list of things to do in San Francisco, with sea lions, waterfront seafood restaurants, top shopping, attractions and bay views.Parking is conveniently available in the Pier 39 Garage located directly across from the Entrance Plaza.',
            "distance":'18',
        },
        {
            "name": 'Lombard Street',
            "description": 'Often called the “crookedest” street in the world, this scenic road on Russian Hill features tight turns, fragrant gardens and beautiful views of the bay, Alcatraz, and Coit Tower.',
            "distance":'19',
        },
        {
            "name": 'The Presidio',
            "description": 'Formerly a military post, the Presidio is now a national park site and recreational paradise featuring spectacular vistas, beautiful trails, and historic and architectural treasures. Come for a hike, a walking tour, a picnic, or to view an exhibit at the Walt Disney Family Museum.',
            "distance":'20',
        },
        {
            "name": 'Yerba Buena Gardens',
            "description": 'An award-winning public facility at the heart of San Francisco’s downtown cultural district, Yerba Buena Gardens features a children’s garden, public art, museums, a historic carousel, ice-skating and bowling centers.',
            "distance":'21',
        },
        {
            "name": 'Contemporary Jewish Museum',
            "description": 'Located in downtown San Francisco, the Contemporary Jewish Museum presents dynamic exhibitions and educational programs, exploring contemporary perspectives on Jewish culture, history and ideas.',
            "distance":'22',
        },
        {
            "name": 'Street Art & Murals',
            "description": 'One of the reasons San Francisco is such a beautiful place to visit is because we have more than 1,000 pieces of street art and murals.The largest concentration of outdoor murals is found in SFs Mission District. More and more pieces are also popping up in Chinatown and North Beach.',
            "distance":'23',
        },
        {
            "name": 'Painted Ladies of Alamo Square',
            "description": 'The Painted Ladies of Alamo Square (also called the "Seven Sisters") are six identical Victorian houses all in a row. The seventh painted lady sits on the northern side of the block and is often included with the six identical houses.Today, thousands of visitors swing by Alamo Square to admire their beauty.',
            "distance":'24',
        },
        {
            "name": 'Japanese Tea Garden',
            "description": 'The Japanese Tea Garden is one of the highly rated San Francisco attractions.You will find it inside Golden Gate Park. Highlights of the Japanese Tea Garden include the arched drum bridge, pagodas, and the Zen garden.You can also spend some time in the tea house sipping on a drink.',
            "distance":'25',
        },
        {
            "name": 'Stairways of SF',
            "description": ' The city has almost 50 named hills and many of them have sets of stairs to get you to the top.Some of the most popular stairs are the 16th Avenue Tiled Stairs, the Hidden Garden Steps and the Lincoln Park Staircase.Other well-traveled stairs include the Filbert and Greenwich Steps that take you to the top of Telegraph Hill where you will find Coit Tower.',
            "distance":'25',
        },
        {
            "name": 'Oracle Park',
            "description": 'Oracle Park is home to San Francisco Giants baseball team. Its one of the best places to catch an MLB game. In addition to baseball games, you will also find a handful of large concerts here every year as well as a free simulcast of a SF Opera performance each summer.',
            "distance":'27',
        },
        {
            "name": 'Coit Tower',
            "description": 'There are two draws to this San Francisco attraction: The first being the historic murals on its walls, which show life in San Francisco in the 1930s. The second is the view from the top of Coit Tower, which offers a 360 degree view of the city.',
            "distance":'28',
        },
        {
            "name": 'Haight-Ashbury',
            "description": 'Often referred to as "The Haight" has been home to people and bands such as the Grateful Dead, Janis Joplin, and Jefferson Airplane. Today, this lively district features dozens of shops, vintage & second-hand clothing stores, and restaurants. Amoeba Records, the worlds largest independent music store is also located here.',
            "distance":'29',
        },
        {
            "name": 'Union Square',
            "description": 'Union Square is the most visited neighborhood in San Francisco. Here you will find a large collection of high end retail outlets, fancy hotels, cafes, art galleries and a very active nightlife.The area has many live events to attend and there is always something happening to keep you entertained.',
            "distance":'30',
        },
        {
            "name": 'Aquarium of the Bay',
            "description": 'Aquarium of the Bay is situated on the waterfront of San Francisco. When you are inside you will see 300 feet of clear tunnels that are full of 700,000 gallons of water. This water sustains 20,000 animals from the bay and surrounding areas. You can come face to face with a leopard shark and be mesmerized by the walls of jellyfish.',
            "distance":'31',
        },
        {
            "name": 'Ferry Building Marketplace ',
            "description": 'Ocean Beach is a beautiful quiet beach with gorgeous white sand and very few tourists. The beach stretches out in front of you for 3.5 miles and often it can just be you, the birds and the ocean waves. The water is good for surfing but only if you are experienced as it can become very choppy.The beach is part of the Golden Gate National Park.',
            "distance":'32',
        },
    ],
}

MY_API = {
    "host": "https://query.yahooapis.com",
    "port": 443,
    "path": "/v1/public/yql?q=select%20*%20from%20weather.forecast%20where%20woeid%20in%20(select%20woeid%20from%20geo.places(1)%20where%20text%3D%22{city}%2C%20{state}%22)&format=json&env=store%3A%2F%2Fdatatables.org%2Falltableswithkeys",
}

