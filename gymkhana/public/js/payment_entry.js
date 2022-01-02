frappe.ui.form.on('Payment Entry', {
	refresh(frm) {
		if(frm.doc.party){
            setTimeout(function(){
                if(frm.doc.member_image)
                    $('[data-fieldname="html_view"]').html('<div class="image text-center" style="height: 130px !important;width: 120px !important;"><img style="max-height: 130px;" src="'+frm.doc.member_image+'"></div>');
            }, 100);   
        }
	},
	party:function(frm){
        $('[data-fieldname="html_view"]').html('');
        if(frm.doc.party){
            setTimeout(function(){
                if(frm.doc.member_image)
                    $('[data-fieldname="html_view"]').html('<div class="image text-center" style="height: 130px !important;width: 120px !important;"><img style="max-height: 130px;" src="'+frm.doc.member_image+'"></div>');
            }, 100);
                
        }
    },
    scan_barcode: function(frm) {
		frm.set_value('party', frm.doc.scan_barcode);
    }
});