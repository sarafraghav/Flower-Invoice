console.log("Sanity check!");
var x = window.location.href.match(/\/([^\/]+)\/?$/)[1];
var y = window.location.href.match(/([^\/]+)\/[^\/]+\/[^\/]+\/?$/)[1];
// Get Stripe publishable key
console.log(x);
fetch("/pconfig/"+x+"/"+y)
.then((result) => { return result.json(); })
.then((data) => {
  // Initialize Stripe.js;
  const stripe = Stripe(data.publicKey, {stripeAccount: data.stripe_account});

  // new
  // Event handler
  document.querySelector("#submitBtn").addEventListener("click", () => {
    // Get Checkout Session ID
    fetch("/pcreate-checkout-session/"+x+"/"+y)
    .then((result) => { return result.json(); })
    .then((data) => {
      console.log(data);
      // Redirect to Stripe Checkout
      return stripe.redirectToCheckout({sessionId: data.sessionId})
    })
    .then((res) => {
      console.log(res);
    });
  });
});