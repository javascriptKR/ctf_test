function newAlert(a)
    {
    window.alert=orgAlert;
    if(a==document.domain)
        {
        if(ok==0)ok=1;
        alert(a);
        window.setInterval(nextstg,500)
    }
    else
        {
        alert(a);
        alert("Please use document.domain!!")
    }
}
window.alert=newAlert;
function nextstg()
    {
    if(ok==1)
        {
            document.all("msg").innerHTML="<span id='h3'>Congratulations!!</span>"+"<a href=/Is_this_the_flag>YOU GET FLAG CLICK.</a>."
        }
        document.all("msg").style.display=""
}
function init() {
    ok=0;
    orgAlert=window.alert;
    window.alert=newAlert;
} 