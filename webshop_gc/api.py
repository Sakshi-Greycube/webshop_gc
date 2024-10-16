import frappe

@frappe.whitelist(allow_guest=True)
def insert_doc(**data):
    print("-----------------Inside Insert Doc----------------")
    try:
        user = ""
        if data.get('data').get('doctype') == "Comment":
            user = frappe.session.user
            data['data']['comment_by'] = user
        
        if data:
            insert_doc = frappe.get_doc({"doctype": data.get('data').get('doctype')})
            insert_doc.update(data.get('data'))
            value = insert_doc.insert(ignore_permissions=True)
            frappe.db.commit()
            return value
    except Exception as e:
        frappe.log_error("Error inserting document: " + str(e))
        return None