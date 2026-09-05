const API_BASE="http://127.0.0.1:8000/api";
async function apiRequest(endpoint,options={}){const r=await fetch(API_BASE+endpoint,{...options});if(!r.ok){let m=`API error ${r.status}`;try{const b=await r.json();m=b.detail||m}catch{}throw new Error(m)}return r.json()}
function moneyINR(v){return new Intl.NumberFormat("en-IN",{style:"currency",currency:"INR",maximumFractionDigits:0}).format(v||0)}
