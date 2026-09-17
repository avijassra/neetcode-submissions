class MinStack {
    #vals;
    #mins;
    
    constructor() {
        this.#vals = [];
        this.#mins = [];
    }

    /**
     * @param {number} val
     * @return {void}
     */
    push(val) {
        this.#vals.push(val);

        let lastMinVal = this.#mins[this.#mins.length-1];

        if(this.#mins.length === 0 || lastMinVal > val) {
            this.#mins.push(val);
        } else {
            this.#mins.push(lastMinVal);
        }
    }

    /**
     * @return {void}
     */
    pop() {
        this.#vals.pop();
        this.#mins.pop();
    }

    /**
     * @return {number}
     */
    top() {
        return this.#vals[this.#vals.length-1];
    }

    /**
     * @return {number}
     */
    getMin() {
        return this.#mins[this.#mins.length-1];
    }
}
