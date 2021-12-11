let canvas = document.getElementById('canvas');
let context = canvas.getContext('2d');

let width = 28;
let height = 28;

//context.scale(10,10);

const lastPosition = { x: null, y: null };
let isDrag = false;

let currentColor = 'rgb(255,255,255)';

// 背景を描画
context.fillStyle = 'rgb(0,0,0)';
context.fillRect(0,0,width,height);

// 線を描画
function draw(x, y) {
    if(!isDrag) {
      return;
    }
    context.lineCap = 'round';
    context.lineJoin = 'round';
    context.lineWidth = 2;
    context.strokeStyle = currentColor;
    if (lastPosition.x === null || lastPosition.y === null) {
      context.moveTo(x, y);
    } else {
      context.moveTo(lastPosition.x, lastPosition.y);
    }
    context.lineTo(x, y);
    context.stroke();

    lastPosition.x = x;
    lastPosition.y = y;
}

function dragStart(event) {
    context.beginPath();

    isDrag = true;
}

    function dragEnd(event) {
    context.closePath();
    isDrag = false;
    lastPosition.x = null;
    lastPosition.y = null;
}

canvas.addEventListener('mousedown', dragStart);
canvas.addEventListener('mouseup', dragEnd);
canvas.addEventListener('mouseout', dragEnd);
canvas.addEventListener('mousemove', (event) => {
    draw(event.layerX, event.layerY);
});


// HTMLフォームの形式にデータを変換する
function EncodeHTMLForm( data )
{
    let params = [];

    for( let name in data )
    {
        let value = data[ name ];
        let param = encodeURIComponent( name ) + '=' + encodeURIComponent( value );

        params.push( param );
    }
    return params.join( '&' ).replace( /%20/g, '+' );
}


function postdata(data){
    let url = '/'; // リクエスト先URL
    let request = new XMLHttpRequest();

    request.open('POST', url);
    request.onreadystatechange = function () {
        if (request.readyState != 4) {
            // リクエスト中
            let dom = document.getElementById('result');
            dom.innerHTML = "判定中...";
        } else if (request.status != 200) {
            // 失敗
            let dom = document.getElementById('result');
            dom.innerHTML = "通信に失敗しました";
        } else {
            // 送信成功
            let result = request.responseText;
            let result_data = JSON.parse(result);

            let dom = document.getElementById('result');
            dom.innerHTML = result_data["result"];
            let dom2 = document.getElementById('softmax');
            dom2.innerHTML = result_data["softmax"];

            console.log(result);
        }
    };
    request.setRequestHeader('Content-Type', 'application/x-www-form-urlencoded');
    request.send(EncodeHTMLForm( data ));
}




let button = document.getElementById('button');
button.addEventListener('click', function(){
    // キャンバスから取得したデータを1x32x32の3次元グレースケール配列に入れなおす
    var img = context.getImageData(0, 0, canvas.width, canvas.height);

    let data = new Array(height);
    for(let y=0; y<height; y++){
        data[y] = new Array(width);
    }
    console.log(img.data.length);

    for(let i=0; i<width*height; i++){
        //console.log(img.data[i*4]);
        data[parseInt(i/width)][i%width] = img.data[i*4];
    }
    console.log([data]);

    // データを送信する
    let posting_data = {
        "key": JSON.stringify([data])
    };
    postdata(posting_data);
    
});
