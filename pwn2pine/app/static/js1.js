const m = {}
const u = new URL(location)
for (const [p, v] of u.searchParams){

    if (!p.includes('[')){
        m[p] = v
        continue
    }
    const [k1, k2] = p.split('[').map(kn => kn.replace(']', ''))

    if (m[k1] === undefined){
        person[k1] = {}
    }
    m[k1][k2] = v
}

const config = {
    theme: 'Default',
    err: 'Error',
    rendered: true
}

if (m.info !== undefined){
    document.getElementById('f').innerHTML = config[m.info]
}else{
    document.getElementById('f').innerHTML = "Goo luck ;p"
}