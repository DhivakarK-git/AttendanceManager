const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const admin = document.getElementById('next');
const container = document.getElementById('container');
const over = document.getElementById('oVER');
const logo = document.getElementById('ER');
const logo1 = document.getElementById('ERL');

var i=1;

container.classList.add('act');
signUpButton.addEventListener('click', () => {
    container.classList.add('right-panel-active');
	container.classList.remove('left-panel-active');
	over.classList.add("is-gx");
	logo.style.opacity=0;
	logo1.style.opacity=1;
    setTimeout(function(){
        over.classList.remove("is-gx");
    }, 1250)
});


signInButton.addEventListener('click', () => {
	container.classList.remove('right-panel-active');
	container.classList.add('left-panel-active');
	over.classList.add("is-gx");
	logo.style.opacity=1;
	logo1.style.opacity=0;
    setTimeout(function(){
        over.classList.remove("is-gx");
    }, 1250)
});

admin.addEventListener('click', () => {
  location. href = "/admin/";
});

document.addEventListener('DOMContentLoaded', function(event) {
	var fade=document.querySelector('body');
	fade.style.opacity = 0;
    var opacity = 0;
	var intervalID = setInterval(function() {
	if (opacity < 0.62 && opacity > 0.38) {
		opacity = opacity + 0.01;
		fade.style.opacity = opacity;
	}

	else if (opacity < 1) {
		opacity = opacity + 0.02;
		fade.style.opacity = opacity;
	}

	else {
			clearInterval(intervalID);
			}
	}, 10);
});

var cache = {};
function loadPage(url) {
  if (cache[url]) {
    return new Promise(function(resolve) {
      resolve(cache[url]);
    });
  }

  return fetch(url, {
    method: 'GET'
  }).then(function(response) {
    cache[url] = response.text();
    return cache[url];
  });
}

var main = document.querySelector('main');

function changePage() {
  var url = window.location.href;

  loadPage(url).then(function(responseText) {
    var wrapper = document.createElement('div');
        wrapper.innerHTML = responseText;

    var oldContent = document.querySelector('.cc');
    var newContent = wrapper.querySelector('.cc');

    main.appendChild(newContent);
    animate(oldContent, newContent);
  });
}

function animate(oldContent, newContent) {
  oldContent.style.position = 'absolute';

  var fadeOut = oldContent.animate({
    opacity: [1, 0]
  }, 1000);

  var fadeIn = newContent.animate({
    opacity: [0, 1]
  }, 1000);

  fadeIn.onfinish = function() {
    oldContent.parentNode.removeChild(oldContent);
  };
}

window.addEventListener('popstate', changePage);

document.addEventListener('click', function(e) {
  var el = e.target;

  while (el && !el.href) {
    el = el.parentNode;
  }

  if (el) {
    e.preventDefault();
    history.pushState(null, null, el.href);
    changePage();

    return;
  }
});
