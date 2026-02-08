// Starfield animation
(function(W, D) {
    "use strict";

    var _cvs = D.getElementById("starfield"),
        _cx  = _cvs.getContext("2d"),
        _stA = [],
        _ssA = [],
        _nS  = 200;

    // Resize canvas to fill window
    function _rC() {
        _cvs.width  = W.innerWidth;
        _cvs.height = W.innerHeight;
    }

    // Create stars
    function _cS() {
        _stA = [];
        for(var i = 0; i < _nS; i++) {
            _stA.push({
                x : Math.random() * _cvs.width,
                y : Math.random() * _cvs.height,
                sz: Math.random() * 2,
                sp: Math.random() * 0.5 + 0.1,
                op: Math.random() * 0.5 + 0.3,
                ts: Math.random() * 0.02 + 0.01,
                td: Math.random() > 0.5 ? 1 : -1
            });
        }
    }

    // Create shooting star
    function _cSS() {
        return {
            x : Math.random() * _cvs.width,
            y : Math.random() * _cvs.height * 0.5,
            l : Math.random() * 80 + 40,
            sp: Math.random() * 15 + 10,
            op: 1,
            a : Math.PI / 4
        };
    }

    // Draw stars
    function _dS() {
        _cx.clearRect(0, 0, _cvs.width, _cvs.height);
        
        for(var i = 0, len = _stA.length; i < len; i++) {
            var s = _stA[i];
            _cx.beginPath();
            _cx.arc(s.x, s.y, s.sz, 0, Math.PI * 2);
            _cx.fillStyle = "rgba(255,255,255," + s.op + ")";
            _cx.fill();
            
            s.y += s.sp;
            if(s.y > _cvs.height) { 
                s.y = 0; 
                s.x = Math.random() * _cvs.width; 
            }
            
            s.op += s.ts * s.td;
            if(s.op > 0.8 || s.op < 0.3) s.td *= -1;
        }
        
        _ssA = _ssA.filter(function(s) { return s.op > 0; });
        for(var j = 0, jl = _ssA.length; j < jl; j++) {
            var ss = _ssA[j];
            _cx.save();
            _cx.translate(ss.x, ss.y);
            _cx.rotate(ss.a);
            
            var g = _cx.createLinearGradient(0, 0, ss.l, 0);
            g.addColorStop(0, "rgba(255,107,107," + ss.op + ")");
            g.addColorStop(1, "rgba(255,107,107,0)");
            
            _cx.strokeStyle = g;
            _cx.lineWidth = 2;
            _cx.beginPath();
            _cx.moveTo(0, 0);
            _cx.lineTo(ss.l, 0);
            _cx.stroke();
            _cx.restore();
            
            ss.x += Math.cos(ss.a) * ss.sp;
            ss.y += Math.sin(ss.a) * ss.sp;
            ss.op -= 0.02;
        }
        
        if(Math.random() < 0.003) _ssA.push(_cSS());
        
        requestAnimationFrame(_dS);
    }

    _rC(); 
    _cS(); 
    _dS();
    
    W.addEventListener("resize", function() { 
        _rC(); 
        _cS(); 
    });

})(window, document);
