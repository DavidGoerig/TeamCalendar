$(document).ready(function(e) {
    let path = window.location.pathname
    let splitted = path.split("/")
    var proj_nbr = splitted[splitted.length - 1]

    var cookiename = "proj" + proj_nbr;
    checkCookie()

    function setInCookie(name,value,exdays) {
        let cookie = getCookie(cookiename)
        if (cookie == "") {
            cookie = ["", "", "", "", "", ""]
            switch (name) {
                case "proj":
                    cookie[0] = value;
                    break;
                case "params":
                    cookie[1] = value;
                    break;
                case "devices":
                    cookie[2] = value;
                    break;
                case "sequence":
                    cookie[3] = value;
                    break;
                case "param_levels":
                    cookie[4] = value;
                    break;
                case "create_seq":
                    cookie[5] = value;
                    break;
            }
        }
        else {
            cookie = cookie.split(":")
            if (cookie.length == 6) {
                switch (name) {
                    case "proj":
                        cookie[0] = value;
                        break;
                    case "params":
                        cookie[1] = value;
                        break;
                    case "devices":
                        cookie[2] = value;
                        break;
                    case "sequence":
                        cookie[3] = value;
                        break;
                    case "param_levels":
                        cookie[4] = value;
                        break;
                    case "create_seq":
                        cookie[5] = value;
                        break;
                }
            }
        }
        let cvalue = cookie.join(':');
        setCookie(cookiename, cvalue, exdays)
    }

    function setCookie(cname,cvalue,exdays) {
        var d = new Date();
        d.setTime(d.getTime() + (exdays*24*60*60*1000));
        var expires = "expires=" + d.toGMTString();
        document.cookie = cname + "=" + cvalue + ";" + expires + ";path=/";
    }
    function getCookie(cname) {
        var name = cname + "=";
        var decodedCookie = decodeURIComponent(document.cookie);
        var ca = decodedCookie.split(';');
        for(var i = 0; i < ca.length; i++) {
            var c = ca[i];
            while (c.charAt(0) == ' ') {
                c = c.substring(1);
            }
            if (c.indexOf(name) == 0) {
                return c.substring(name.length, c.length);
            }
        }
        return "";
    }

    function checkCookie() {
        let cookie = getCookie(cookiename)
        cookie = cookie.split(":")
            if (cookie.length == 6) {
                if (cookie[0] == "show") {
                    $("#proj").toggle();
                }
                if (cookie[1] == "show") {
                    $("#params").toggle();
                }
                if (cookie[2] == "show") {
                    $("#devices").toggle();
                }
                if (cookie[3] == "show") {
                    $("#sequence").toggle();
                }
                if (cookie[4] == "show") {
                    $("#param_levels").toggle();
                }
                if (cookie[5] == "show") {
                    $("#createseq").toggle();
                }
            }
    }

    $("#toggle_proj").click(function(){
            $("#proj").toggle();
            if  ( $("#proj").is(":hidden") ){
                setInCookie("proj", "", 1);
            }
            else {
                setInCookie("proj", "show", 1);
            }
        });

    $("#toggle_params").click(function(){
            $("#params").toggle();
            if  ( $("#params").is(":hidden") ){
                setInCookie("params", "", 1);
            }
            else {
                setInCookie("params", "show", 1);
            }
        });

    $("#toggle_devices").click(function(){
            $("#devices").toggle();
            if  ( $("#devices").is(":hidden") ){
                setInCookie("devices", "", 1);
            }
            else {
                setInCookie("devices", "show", 1);
            }
        });

    $("#toggle_sequence").click(function(){
            $("#sequence").toggle();
            if  ( $("#sequence").is(":hidden") ){
                setInCookie("sequence", "", 1);
            }
            else {
                setInCookie("sequence", "show", 1);
            }
        });

    $("#toggle_param_levels").click(function(){
            $("#param_levels").toggle();
            if  ( $("#param_levels").is(":hidden") ){
                setInCookie("param_levels", "", 1);
            }
            else {
                setInCookie("param_levels", "show", 1);
            }
        });

    $("#toggle_createseq").click(function(){
            $("#createseq").toggle();
            if  ( $("#createseq").is(":hidden") ){
                setInCookie("create_seq", "", 1);
            }
            else {
                setInCookie("create_seq", "show", 1);
            }
        });
});