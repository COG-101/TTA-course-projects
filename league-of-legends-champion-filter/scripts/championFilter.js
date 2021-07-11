const championContainer = document.querySelector('.champion-container'); //var of the whole champ section
const filterButtons = document.querySelectorAll('.filter-button'); //var of all filter buttons

function displayChamps(champList){ //To display all menu items on page
    let displayChamps = champList.map(function(item){ //creates a new array of all the champs, takes the info from the const and adds it into template html for the page.
        return `<div>
                    <a href=${item.link} target='_blank'>
                        <img class='champ-image' src=${item.img} alt=${item.title}>
                    </a>
                    <h3 class='champ-name'>${item.title}</h3>
                </div>`
    })

    displayChamps = displayChamps.join('');
    console.log(displayChamps);
    championContainer.innerHTML = displayChamps; //adds array of champs and adds them to the champ container    
};


window.addEventListener('DOMContentLoaded', function(){ //actions when page has fully loaded
    displayChamps(champs);
});


filterButtons.forEach(function (btn) {
    btn.addEventListener('click', function (e){ //when clicked do this function with e as the parameter
        const role = e.currentTarget.dataset.id; // get value of e
        const roleCategory = champs.filter(function (champion){ //return champs when their role matches
            if (champion.role === role) {
                return champion;
            }
        });

        if (role === 'all') {
            displayChamps(champs)
        } else { //show only those whose role matches the clicked button's value
            displayChamps(roleCategory)
        }
    });
});



const champs = [
    {
        id: 1,
        title: 'Aatrox',
        role: 'top',
        img: 'img/champ-images/aatrox.jpg',
        link: 'https://na.leagueoflegends.com/en-us/champions/aatrox/'
    },
    {       
        id: 2,
        title: 'Ashe',
        role: 'bottom',
        img: 'img/champ-images/ashe.jpg',
        link: 'https://na.leagueoflegends.com/en-us/champions/ashe/'
    },
    {       
        id: 3,
        title: 'Cho\'gath',
        role: 'top',
        img: 'img/champ-images/chogath.jpg',
        link: 'https://na.leagueoflegends.com/en-us/champions/cho-gath/'
    },
    {       
        id: 4,
        title: 'Galio',
        role: 'mid',
        img: 'img/champ-images/galio.jpg',
        link: 'https://na.leagueoflegends.com/en-us/champions/galio/'
    },
    {
        id: 5,
        title: 'Kayle',
        role: 'middle',
        img: 'img/champ-images/kayle.jpg',
        link: 'https://na.leagueoflegends.com/en-us/champions/kayle/'
    },
    {       
        id: 6,
        title: 'Lee Sin',
        role: 'jungle',
        img: 'img/champ-images/leesin.jpg',
        link: 'https://na.leagueoflegends.com/en-us/champions/lee-sin/'
    },
    {
        id: 7,
        title: 'Lucian',
        role: 'bottom',
        img: 'img/champ-images/lucian.jpg',
        link: 'https://na.leagueoflegends.com/en-us/champions/lucian/'
    },
    {
        id: 8,
        title: 'Malzahar',
        role: 'middle',
        img: 'img/champ-images/malzahar.jpg',
        link: 'https://na.leagueoflegends.com/en-us/champions/malzahar/'
    },
    {
        id: 9,
        title: 'Morgana',
        role: 'support',
        img: 'img/champ-images/morgana.jpg',
        link: 'https://na.leagueoflegends.com/en-us/champions/morgana/'
    },
    {
        id: 10,
        title: 'Nocturne',
        role: 'jungle',
        img: 'img/champ-images/nocturne.jpg',
        link: 'https://na.leagueoflegends.com/en-us/champions/nocturne/'
    },
    {
        id: 11,
        title: 'Ornn',
        role: 'top',
        img: 'img/champ-images/ornn.jpg',
        link: 'https://na.leagueoflegends.com/en-us/champions/ornn/'
    },
    {
        id: 12,
        title: 'Soraka',
        role: 'support',
        img: 'img/champ-images/soraka.jpg',
        link: 'https://na.leagueoflegends.com/en-us/champions/soraka/'
    },
    {
        id: 13,
        title: 'Swain',
        role: 'bottom',
        img: 'img/champ-images/swain.jpg',
        link: 'https://na.leagueoflegends.com/en-us/champions/swain/'
    },
    {
        id: 14,
        title: 'Talon',
        role: 'jungle',
        img: 'img/champ-images/talon.jpg',
        link: 'https://na.leagueoflegends.com/en-us/champions/talon/'
    },
    {
        id: 15,
        title: 'Thresh',
        role: 'middle',
        img: 'img/champ-images/thresh.jpg',
        link: 'https://na.leagueoflegends.com/en-us/champions/thresh/'
    },
    {
        id: 16,
        title: 'Urgot',
        role: 'top',
        img: 'img/champ-images/urgot.jpg',
        link: 'https://na.leagueoflegends.com/en-us/champions/urgot/'
    },
    {
        id: 17,
        title: 'Wukong',
        role: 'jungle',
        img: 'img/champ-images/wukong.jpg',
        link: 'https://na.leagueoflegends.com/en-us/champions/wukong/'
    }
];