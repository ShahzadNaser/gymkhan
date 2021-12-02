frappe.ui.form.on('Payment Entry', {
	refresh(frm) {
        console.log("=============================");
		if(frm.doc.party){
            setTimeout(function(){
                if(frm.doc.member_image)
                    $('[data-fieldname="html_view"]').html('<div class="image text-center" style="height: 100px !important;width: 120px !important;"><img src="'+frm.doc.member_image+'"></div>');
            }, 100);
                
        }
	},
	party:function(frm){
        $('[data-fieldname="html_view"]').html('');
        console.log("=============================");
        if(frm.doc.party){
            setTimeout(function(){
                if(frm.doc.member_image)
                    $('[data-fieldname="html_view"]').html('<div class="image text-center" style="height: 100px !important;width: 120px !important;"><img src="'+frm.doc.member_image+'"></div>');
            }, 1000);
                
        }
    }
})