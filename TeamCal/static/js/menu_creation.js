$(document).ready(function(e) {
    // define the path of the xml
    let path_to_xml =  "/static/conf_file/menu_para_file.xml"

    var $xml = load_xml(path_to_xml);
    let menu_info = get_menu_information();
    let brand_string = brand_string_creation(menu_info);
    let button_string = button_string_creation(menu_info);

    $('#sidebarCollapse').on('click', function () {
        $('#sidebar').toggleClass('active');
        $('#content').toggleClass('active');
    });

    create_menu(brand_string, button_string);

    function top_bar_string_creation(menu_info) {
    let topbar_string = '<ul class="nav navbar-nav ml-auto">'
    let navbarexist = $xml.find("navbar");
    if (navbarexist) {
        let buttnbr = Number(navbarexist.find("buttonnbr").text())
        for (let i = 0; i < buttnbr; i++) {
            let buttnbrstr = "navbutton" + i
            topbar_string += '<li class="nav-item"><a class="nav-link" href="'
            topbar_string += menu_info.domain + navbarexist.find(buttnbrstr).find("hrefdrop").text()
            topbar_string += '"><span class="navbar-btn-txt">'
            topbar_string += navbarexist.find(buttnbrstr).find("textdrop").text()
            topbar_string += '</span></a></li>'
        }
    }
    topbar_string += '<img src="/static/img/icons/roche-logo.png" class="rocheicone" width="55px" height="30px">'
    topbar_string += '</ul>'
    return topbar_string
}
    
    /*
    **  fct name: brand_string_creation
    **  input: menu_info structure -> let menu_info = {
            nbrbutton: 0,
            colorbutton: "#ffffff",
            colortxtbutton: "#000",
            icone: "svg",
            iconetext: "Default",
            index: "hrefindex",
            error: false
        };
    **  output:     string with the brand string of the navbar
    */

   function brand_string_creation(menu_info) {
    let brand_string = '<div class="sidebar-header"><a href="' + menu_info.index + '">'
    brand_string += '<h3>' +'<i class="'
    brand_string += menu_info.icone
    brand_string += ' fa facolor"></i> '
    brand_string += menu_info.iconetext + '</h3>'
    brand_string += '<strong>' +'<i class="'
    brand_string += menu_info.icone
    brand_string += ' fa facolor"></i></strong></a></div>'
    return brand_string
}

    /*
    **  fct name: button_string_creation
    **  input: menu_info structure -> let menu_info = {
            nbrbutton: 0,
            colorbutton: "#ffffff",
            colortxtbutton: "#000",
            icone: "svg",
            iconetext: "Default",
            index: "hrefindex",
            error: false
        };
    **  output:     string with the button string of the navbar
    */

    function button_string_creation(menu_info) {
        let button_string = ''
        for (let i = 0; i < menu_info.nbrbutton; i++) {
            let buttonnbr = "button" + i;
            let buttonexist = $xml.find(buttonnbr);
            let dropdown = buttonexist.find("dropdownnbr").text()
            if (dropdown) {
                if (Number(dropdown)){
                    button_string +=  create_button_with_dropdown(buttonexist, dropdown, menu_info)
                }
                else {
                    button_string +=  create_button_without_dropdown(buttonexist, menu_info)
                }
            }
            else {
                // button don't exist
                console.log("False button setup, menu failed to build.")
            }
            /*if (Number(dropdown)){
                menu_info.nbrbutton = nbrbutton
            }*/
        }
        return button_string
    }

    /*
    **  fct name: create_button_without_dropdown
    **  input: buttonexist : xml with the button file
    **  output:     the navbar button string
    */

    function create_button_without_dropdown(buttonexist, menu_info) {
        let button_string = '<li><a href="'
        button_string += menu_info.domain + buttonexist.find("href").text()
        button_string += '">'
        button_string += '<i class="'
        button_string += buttonexist.find("icone").text()
        button_string += ' fa-lg facolor"></i><br>'
        button_string += buttonexist.find("text").text()
        button_string += '</a></li>'
        return button_string
    }

    /*
    **  fct name: create_button_with_dropdown
    **  input: buttonexist : xml with the button file
    **  output:     the navbar button string
    */

    function create_button_with_dropdown(buttonexist, dropdown, menu_info) {
        let button_string = '<li><a class="dropdown-toggle" href="#' + buttonexist.find("href").text()
        button_string += 'Submenu" data-toggle="collapse" aria-expanded="false">'
        button_string += '<i class="'
        button_string += buttonexist.find("icone").text()
        button_string += ' fa-lg facolor"></i><br>'
        button_string += buttonexist.find("text").text() + '</a><ul class="collapse list-unstyled" id="' + buttonexist.find("href").text() + 'Submenu">'
        for (let i = 0; i < dropdown; i++) {
            let dropnbr = "dropdown" + i
            button_string += '<a href="'
            button_string += menu_info.domain + buttonexist.find(dropnbr).find("hrefdrop").text()
            button_string += '"><li>'
            button_string += buttonexist.find(dropnbr).find("textdrop").text()
            button_string += '</li></a>'
        }

        button_string += '</ul></li>'
        return button_string
    }


    /*
    **  fct name: create_menu
    **  input: button_string -> (string) string containing the button html string created with the list
    **  output:     /
    */

    function create_menu(brand_string, button_string, top_bar_string) {
        let sidebar_string = brand_string
        sidebar_string += '<ul class="list-unstyled components">'
        sidebar_string += button_string
        sidebar_string += '</ul>'
        $('#sidebar').empty().html(sidebar_string);
    }
    
    /*
    **  fct name: get_menu_information
    **  input: /
    **  output:     - nbrbutton = int containing the number of button in the menu
                    - colorbutton = string containing the color of buttons of the menu
                    - colortxtbutton = string containing the color of the texts in the buttons of the menu
                    - icone = string contraining the string of the icone
                    - iconetext = the text after the icone
    */

    
    function get_menu_information () {
        let infomenu = $xml.find("infomenu");
        let menu_info = {
            nbrbutton: 0,
            colorbutton: "#ffffff",
            colortxtbutton: "#000",
            icone: "svg",
            iconetext: "Default",
            index: "#",
            error: false,
            domain: "/"
        };
        let nbrbutton = infomenu.find("nbrbutton").text();
        if (Number(nbrbutton)){
            menu_info.nbrbutton = nbrbutton
        }
        let colorbutton = infomenu.find("colorbutton").text();
        if (typeof(colorbutton) == "string") {
            menu_info.colorbutton = colorbutton
        }
        let domain = infomenu.find("domain").text();
        if (typeof(domain) == "string") {
            menu_info.domain = domain
        }
        let colortxtbutton = infomenu.find("colortxtbutton").text();
        if (typeof(colortxtbutton) == "string") {
            menu_info.colortxtbutton = colortxtbutton
        }
        let icone = infomenu.find("icone").text();
        if (typeof(icone) == "string") {
            menu_info.icone = icone
        }
        let iconetext = infomenu.find("iconetext").text();
        if (typeof(iconetext) == "string") {
            menu_info.iconetext = iconetext
        }
        let index = infomenu.find("index").text();
        if (typeof(index) == "string") {
            menu_info.index = index
        }
        return menu_info
    }

    /*
    **  fct name: load_xml
    **  input: path_to_xml -> (string) string containing path to the xml
    **  output:     -xml -> object containing the xml
    */

    function load_xml(path_to_xml) {
        // Create a connection to the file.
        var Connect = new XMLHttpRequest();
        // Define which file to open and
        // send the request.
        Connect.open("GET", path_to_xml, false);
        Connect.setRequestHeader("Content-Type", "text/xml");
        Connect.send(null);
        var xml = Connect.responseText,
            xmlDoc = $.parseXML( xml ),
            $xml = $( xmlDoc )


        //let    xmlDoc = $.parseXML( xml_file ),
        //    $xml = $( xmlDoc )
        return $xml
    }

});
