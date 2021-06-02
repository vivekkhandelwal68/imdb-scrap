# imdb-scrap

In this project, I have tried to scrap IMDB Website. 
All we need to do is provide director link and file name in app.py file as given below.

For Example, I want scrap all movies which is related to Michael Bay

So In app.py file, give the value of below given varaibles

file_name = <output_path/file_name> eg. 'output/bayDB.json'
main_url = <Director Link> eg. 'https://www.imdb.com/name/nm0000881/?ref_=nv_sr_srsg_0'

Now just run the app.py file and you will find output file in output folder

Sample Output:

[
{
  "@context": "https://schema.org",
  "@type": "Movie",
  "url": "/title/tt14371860/",
  "name": "Apartment 7A",
  "genre": [
    "Horror",
    "Thriller"
  ],
  "director": [
    {
      "@type": "Person",
      "url": "/name/nm4013000/",
      "name": "Natalie Erika James"
    }
  ],
  "creator": [
    {
      "@type": "Organization",
      "url": "/company/co0071240/"
    },
    {
      "@type": "Organization",
      "url": "/company/co0149632/"
    },
    {
      "@type": "Person",
      "url": "/name/nm4013000/",
      "name": "Natalie Erika James"
    },
    {
      "@type": "Person",
      "url": "/name/nm1671998/",
      "name": "Skylar James"
    },
    {
      "@type": "Person",
      "url": "/name/nm2021376/",
      "name": "Christian White"
    }
  ]
},
{
  "@context": "https://schema.org",
  "@type": "Movie",
  "url": "/title/tt13857278/",
  "name": "Armored",
  "genre": [
    "Action",
    "Thriller"
  ],
  "creator": [
    {
      "@type": "Person",
      "url": "/name/nm3892675/",
      "name": "Mark Greaney"
    }
  ]
},
{
  "@context": "https://schema.org",
  "@type": "Movie",
  "url": "/title/tt6465742/",
  "name": "Little America",
  "genre": [
    "Action",
    "Adventure",
    "Sci-Fi"
  ],
  "actor": [
    {
      "@type": "Person",
      "url": "/name/nm0000230/",
      "name": "Sylvester Stallone"
    }
  ],
  "director": [
    {
      "@type": "Person",
      "url": "/name/nm1424282/",
      "name": "Rowan Athale"
    }
  ],
  "creator": [
    {
      "@type": "Organization",
      "url": "/company/co0690042/"
    },
    {
      "@type": "Organization",
      "url": "/company/co0053925/"
    },
    {
      "@type": "Organization",
      "url": "/company/co0071240/"
    },
    {
      "@type": "Person",
      "url": "/name/nm1424282/",
      "name": "Rowan Athale"
    }
  ],
  "description": "In a dystopian future where China owns America, a former American Force Recon member is hired by a Chinese billionaire to go to an American ghetto and find his daughter.",
  "keywords": "future"
},
{
.
.

.
.
.
.
