
const _AVAILABLE_PRODUCTS = require('../db.json').items.map(e => ({
    ...e
}));

const _CART_ITEMS = [
    {
        "name": "Leite",
        "price": 5.50,
        "measure": "caixinha"
    },
];

const loadAvailableProducts = () => {
    const promisse = new Promise((resolve, reject) => {
        setTimeout(() => {
            resolve(_AVAILABLE_PRODUCTS);
        }, 1000);
    });
    return promisse;
}

const loadCart = () => {
    const promisse = new Promise((resolve, reject) => {
        setTimeout(() => {
            let total = 0;
            _CART_ITEMS.forEach(item => {
                total += item.price;
            });
            resolve({
                items: _CART_ITEMS,
                total: total,
            });
        }, 1000);
    });
    return promisse;
}

const addItemToCart = (product) => {
    const promisse = new Promise((resolve, reject) => {
        const item = {
            name: product.name,
            price: product.price,
            measure: product.measure,
        };
        setTimeout(() => {
            _CART_ITEMS.push(item)
            resolve(item);
        }, 1000);
    });
    return promisse;
}

const removeItemToCart = () => {
    const promisse = new Promise((resolve, reject) => {

    });
    return promisse;
}

export default {
    loadAvailableProducts,
    loadCart,
    addItemToCart,
    removeItemToCart,
}
