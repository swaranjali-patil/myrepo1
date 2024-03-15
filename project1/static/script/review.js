// const allStar = document.querySelectorAll('.rating .star')
// const ratingValue = document.querySelector('.rating input')

// allStar.forEach((item, idx)=> {
// 	item.addEventListener('click', function () {
// 		let click = 0
// 		ratingValue.value = idx + 1

// 		allStar.forEach(i=> {
// 			i.classList.replace('fas-star', 'fa-star')
// 			i.classList.remove('active')
// 		})
// 		for(let i=0; i<allStar.length; i++) {
// 			if(i <= idx) {
// 				allStar[i].classList.replace('fa-star', 'fas-star')
// 				allStar[i].classList.add('active')
// 			} else {
// 				allStar[i].style.setProperty('--i', click)
// 				click++
// 			}
// 		}
// 	})
// })


const stars = document.querySelectorAll(".stars i");
stars.forEach((star, index1) => {
	star.addEventListener("click",() => {
			stars.forEach((star, index2) => {
				index1 >= index2 ? star.classList.add("active"): star.classList.remove("active");
			})
		})
	})