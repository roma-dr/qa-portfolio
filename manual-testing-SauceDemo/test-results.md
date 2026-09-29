# Test Execution Summary — Sauce Demo

**Application:** https://www.saucedemo.com  
**Browser:** Chrome, Safari  

## Summary

| Metric              | Count |
|---------------------|-------|
| Total test cases    | 35    |
| Passed              | 22    |
| Failed              | 13    |
| Bugs found          | 15    |

## Results by Module

### Login
- Standard positive and negative cases — **Passed**
- `locked_out_user`, empty fields, wrong password — **Passed** (errors match expected)
- Special users (`problem_user`, `error_user`, `visual_user`, `performance_glitch_user`) — **Passed with issues** (login works, but further functionality is broken)

### Products
- Display of products — **Passed** (`standard_user`)
- Sorting — **Failed** on `problem_user` and `error_user`
- Add to cart from list — **Passed** on `standard_user`
- Product images and details — **Failed** on `problem_user` and `visual_user`

### Cart
- Add / remove / open cart — **Passed** on `standard_user`
- Empty cart checkout — **Failed** (BUG-001)

### Checkout
- Full successful flow — **Passed** on `standard_user`
- Field validation — **Passed** on `standard_user`
- Form field issues — **Failed** on `problem_user` and `error_user`

### Special Users
- `problem_user` — multiple functional and UI bugs
- `error_user` — sorting error + input field problems
- `visual_user` — layout and price issues
- `performance_glitch_user` — significant delays

## Conclusion

Main user flow works correctly with `standard_user`.  
Most critical issues appear when using special demo accounts, which is expected for this training application.  
One high-severity issue was found on the main flow: ability to complete checkout with an empty cart (BUG-001).