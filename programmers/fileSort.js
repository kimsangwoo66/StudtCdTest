function solution(files) {
  return files.sort((a,b) => {

    var aHead = a.match(/^\D+/)[0].toLowerCase()
    var bHead = b.match(/^\D+/)[0].toLowerCase()


    if(aHead < bHead) {
      return -1
    }
    if(aHead > bHead) {
      return 1
    }

    var anum = a.match(/\d+/)[0].replace(/^0+/, '')
    var bnum = b.match(/\d+/)[0].replace(/^0+/, '')

    return anum - bnum
  })
}



var files = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]

var result = solution(files)

