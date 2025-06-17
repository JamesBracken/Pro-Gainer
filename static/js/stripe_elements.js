// The javascript in this file was done with guidance from
// The code institute boutique ado guide https://www.youtube.com/watch?v=eUcMh5s_27I&t=456s
const stripePublicKey = $("#id_stripe_public_key").text().slice(1, -1);
let clientSecret = $("#id_client_secret").text().slice(1, -1);
const stripe = Stripe(stripePublicKey);
const elements = stripe.elements();

const style = {
  base: {
    color: '#000',
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: 'antialiased',
    fontSize: '16px',
    '::placeholder': {
      color: '#aab7c4'
    }
  },
  invalid: {
    color: '#dc3545',
    iconColor: '#dc3545'
  }
};
const card = elements.create("card", { style: style });
card.mount("#card-element");

// Handle the card element validation errors

card.addEventListener("change", function (event) {
  const errorDiv = document.getElementById("card-errors");
  if (event.error) {
    const html = `
    <span class="icon: role="alert">
    <i class="fas fa-times"></i>
    </span>
    <span>${event.error.message}</span>`

    $(errorDiv).html(html);
  } else {
    errorDiv.textContent = "";
  }

});

// Handle form submission
const form = document.getElementById("payment-form")

form.addEventListener("submit", function (event) {
  // Prevent form submission
  event.preventDefault();
  card.update({ "disabled": true });
  $("#submit-button").attr("disabled", true);
  // Send code to stripe
  stripe.confirmCardPayment(clientSecret, {
    payment_method: {
      card: card,
    }
  }).then(function (result) {
    if (result.error) {
      const errorDiv = document.getElementById("card-errors");
      const html = `
        <span class="icon: role="alert">
        <i class="fas fa-times"></i>
        </span>
        <span>${result.error.message}</span>`;
      $(errorDiv).html(html);
      card.update({ "disabled": false });
      $("#submit-button").attr("disabled", false);
    } else {
      if (result.paymentIntent.status === "succeeded") {
        form.submit();
      }
    }
  })

})