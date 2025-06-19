// GLOBAL VARIABLES PLACED HERE AT THE TOP OF THE CODE
// CONSTANT VARIABLES
const membershipLengthFormField = document.getElementById("id_membership_length")
const membershipCostsParagraph = document.getElementById("membership-costs")
const joiningFeeParagraph = document.getElementById("joining-fee")
const grandTotalParagraph = document.getElementById("grand-total")

// EVENT LISTENERS
membershipLengthFormField.addEventListener("change", updateMembershipCosts)
membershipLengthFormField.addEventListener("change", updateMembershipsCostsSession)
// FUNCTIONS

// As we currently only have one membership type the function does not currently need to
// account for the membership type. Future iterations would adjust prices
// for each different membership type
/* This function updates the payment summary on the membership_form page.
   When the membership length input field is changed the function invokes and
   updates the costs displayed.

   No parameters are in user for this function
*/
function updateMembershipCosts(){
    // Setting the value from the field to number
    membershipPeriodValue = Number(membershipLengthFormField.value);
    // These may be better on const but the prices can change 
    // so I used let instead
    let threeMonthsMembershipFee = 120;
    let twelveMonthsMembershipFee = 399;
    let joiningFee = 0
    // Display all the Membership costs
    if (membershipPeriodValue === 3) {
        grandTotal = threeMonthsMembershipFee + joiningFee
        membershipCostsParagraph.innerHTML = `£${threeMonthsMembershipFee}`;
        joiningFeeParagraph.innerHTML = `<strong>£${joiningFee}</strong>`;
        grandTotalParagraph.innerHTML = `£${grandTotal}`;
    } else if (membershipPeriodValue === 12){
        grandTotal = twelveMonthsMembershipFee + joiningFee
        membershipCostsParagraph.innerHTML = `£${twelveMonthsMembershipFee}`;
        joiningFeeParagraph.innerHTML = `<strong>£${joiningFee}</strong>`;
        grandTotalParagraph.innerHTML = `£${grandTotal}`;
    }
};

/* This function creates a session each time the membership length field changes.
   The session will contain the value of the input field and will be handled in
   the backend with django for security purposes.

*@param {Click} e - This is information of the event that triggers the
 function

*/
function updateMembershipsCostsSession(e) {
    fetch("/store-membership-length", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": csrfToken,
        },
        body:JSON.stringify({
            selected_membership_length: e.target.value
        })
    });
};