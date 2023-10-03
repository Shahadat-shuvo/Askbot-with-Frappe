// Copyright (c) 2023, shuvo and contributors
// For license information, please see license.txt

frappe.ui.form.on('My Maps', {
	city: function(frm) {
	  // Set the default city value
	  	
		let inputs = frm.doc.city;
		frappe.call({
			method: 'maps.maps.doctype.my_maps.my_maps.get_response',
			args: {
				'user_inputs': inputs
			},
			callback: function(r) {
				// console.log(r);
				let responses = r.message; // Assuming you have an input field with the id 'city-input'
				// frm.set_value('city', responses);
				frm.set_df_property('street', 'options', responses[0]);
				frm.refresh()

				console.log(responses);
				
					}
				})

		},
		onload: function(frm) {
		
			cur_frm.fields_dict.street.$input.on("keypress", function(evt){
				// Code specified here will run when a key is pressed on the customer field.
					frm.doc.city = "BD";
				});
			}
	
		
		
	});

	


	
	
  