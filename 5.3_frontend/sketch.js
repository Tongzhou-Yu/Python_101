let binId = null;
let accessKey = null;
let data = null;
let isLoading = false;
let isConnected = false;
let pollInterval = null;

function setup() {
    createCanvas(800, 600);
    textAlign(CENTER, CENTER);
}

function startConnection() {
    binId = document.getElementById('binId').value.trim();
    accessKey = document.getElementById('accessKey').value.trim();
    
    if (!binId || !accessKey) {
        document.getElementById('status').textContent = '请填写 Bin ID 和 Access Key';
        document.getElementById('status').style.color = '#f44336';
        return;
    }
    
    isConnected = true;
    document.getElementById('status').textContent = '已连接，正在加载数据...';
    document.getElementById('status').style.color = '#4CAF50';
    
    loadData();
    
    if (pollInterval) {
        clearInterval(pollInterval);
    }
    pollInterval = setInterval(loadData, 2000);
}

function draw() {
    background(240);
    
    if (!isConnected) {
        fill(150);
        textSize(20);
        text('请在上方输入 Bin ID 和 Access Key 后点击连接', width/2, height/2);
        return;
    }
    
    if (isLoading) {
        fill(100);
        text('加载中...', width/2, height/2);
        return;
    }
    
    if (data) {
        fill(0);
        textSize(24);
        text('最新消息:', width/2, 100);
        
        fill(50);
        textSize(18);
        text(data.text || '无数据', width/2, 200);
        
        if (data.timestamp) {
            fill(150);
            textSize(14);
            text('时间: ' + new Date(data.timestamp).toLocaleString('zh-CN'), width/2, 250);
        }
        
        let radius = map(data.text ? data.text.length : 0, 0, 100, 20, 150);
        fill(100, 150, 255, 100);
        noStroke();
        circle(width/2, height/2 + 50, radius);
    }
}

async function loadData() {
    if (!isConnected || !binId || !accessKey || isLoading) return;
    
    isLoading = true;
    try {
        let response = await fetch(`https://api.jsonbin.io/v3/b/${binId}/latest`, {
            headers: {
                'X-Access-Key': accessKey
            }
        });
        
        if (response.ok) {
            let result = await response.json();
            data = result.record;
            document.getElementById('status').textContent = '连接成功';
            document.getElementById('status').style.color = '#4CAF50';
        } else {
            document.getElementById('status').textContent = '加载失败: ' + response.status;
            document.getElementById('status').style.color = '#f44336';
        }
    } catch (error) {
        console.error('加载失败:', error);
        document.getElementById('status').textContent = '连接错误: ' + error.message;
        document.getElementById('status').style.color = '#f44336';
    }
    isLoading = false;
}

async function saveData(text) {
    if (!isConnected || !binId || !accessKey) return;
    
    try {
        let payload = {
            text: text,
            timestamp: new Date().toISOString(),
            read: false
        };
        
        let response = await fetch(`https://api.jsonbin.io/v3/b/${binId}`, {
            method: 'PUT',
            headers: {
                'X-Access-Key': accessKey,
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(payload)
        });
        
        if (response.ok) {
            console.log('保存成功');
            loadData();
        } else {
            document.getElementById('status').textContent = '保存失败: ' + response.status;
            document.getElementById('status').style.color = '#f44336';
        }
    } catch (error) {
        console.error('保存失败:', error);
        document.getElementById('status').textContent = '保存错误: ' + error.message;
        document.getElementById('status').style.color = '#f44336';
    }
}

function mousePressed() {
    if (!isConnected) return;
    if (mouseX > 0 && mouseX < width && mouseY > 0 && mouseY < height) {
        saveData(`点击位置: (${mouseX}, ${mouseY})`);
    }
}

