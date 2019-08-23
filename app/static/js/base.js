function Register(){
	let name = $("#nameReg").val();
	let phone = $("#phoneReg").val();
	let password = $("#passwordReg").val();
	let data = {};
	data.name = name;
	data.phone = phone;
	data.password = password;
	let url = "/register/";
	let succ1 = "Registered Successfully.";
	let succ2 = "Please login now";
	let fail1 = "Something went wrong.";
	let fail2 = "Please check the details entered.";
	let redirectTo = "";
	UseAjax(url, data, succ1, succ2, fail1, fail2, redirectTo);
}

function Login(){
	let phone = $("#phoneLog").val();
	let password = $("#passwordLog").val();
	let data = {};
	data.phone = phone;
	data.password = password;
 	let url = "/login/";
	let succ1 = "Verification successful";
	let succ2 = "";
	let fail1 = "Verification error.";
	let fail2 = "Please try again";
	let redirectTo = "/my_notes/";
	UseAjax(url, data, succ1, succ2, fail1, fail2, redirectTo);
}

function Search(){
	var toFind = $("#toSearch").val();
	alert(toFind);
}

function SaveNote(){
	let url = "/add_new_note/";
	var newNote = $("#newNote").val();
	let data = {};
	data.newNote = newNote;
	let succ1 = "Note added Successfully";
	let succ2 = "";
	let fail1 = "Something went wrong";
	let fail2 = "Please try again.";
	let redirectTo = "/my_notes/";
	UseAjax(url, data, succ1, succ2, fail1, fail2, redirectTo);
}

function UpdateNote(){
	let noteId = $("#myNoteId").html();
	let noteVal = $("#myNote").val();
	let url = "/update_note/";
	let data = {};
	data.noteId = noteId;
	data.updatedNote = noteVal;
	let succ1 = "Note Updated Successfully";
	let succ2 = "";
	let fail1 = "Something went wrong";
	let fail2 = "Please try again later";
	let redirectTo = "";
	UseAjax(url, data, succ1, succ2, fail1, fail2, redirectTo);
}

function DeleteNote(noteId){
	let url = "/delete_note/";
	let data = {};
	data.noteId = noteId;
	let succ1 = "Note deleted Successfully";
	let succ2 = "";
	let fail1 = "Something went wrong.";
	let fail2 = "Please try again later.";
	let redirectTo = "";
	UseAjax(url, data, succ1, succ2, fail1, fail2, redirectTo);
}

function UseAjax(url, data, succ1, succ2, fail1, fail2, redirectTo){
	$.ajax({
		type: "POST",
		url: url,
		async: false,
		data: {'data': JSON.stringify(data)},
		success: function(response){
			console.log(response, typeof(response));
			swal({
				title: succ1,
				text: succ2,
				icon: 'success',
			}).then(function(){
				if(redirectTo==""){
					window.location.reload();
				}else{
					window.location.href = redirectTo;
				}
			});
		},
		error: function(response){
			console.log(response.status);
			swal({
				title: fail1,
				text: fail2,
				icon: 'error',
			}).then(function(){
				window.location.reload();
			})
		}
	});
}

function ReadNote(noteVal){
	$('#myNoteModal').modal('show');
	$("#myNoteTitle").html("Read Note");
	$("#updateBtn").hide();
	$("#myNote").val(noteVal);
	$("#myNote").prop('disabled', true);
}

function EditNote(noteId, noteVal){
	$('#myNoteModal').modal('show');
	$("#myNoteTitle").html("Edit Note");
	$("#myNoteId").html(noteId);
	$("#updateBtn").show();
	$("#myNote").val(noteVal);
	$("#myNote").prop('disabled', false);
}