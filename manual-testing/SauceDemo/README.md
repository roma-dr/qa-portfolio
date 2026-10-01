# Manual Testing — Sauce Demo

Manual QA testing project for the demo e-commerce application [Sauce Demo](https://www.saucedemo.com).

## Overview

This project covers functional testing of the main user flows:
- Login (all demo users)
- Products (display, sorting, add to cart)
- Cart
- Checkout
- Negative scenarios and special demo users

The goal is to practice test case design, bug reporting, and smoke testing.

## Test Coverage

### Login
- Successful login with `standard_user`
- Locked out user
- Invalid credentials and empty fields
- Special users: `problem_user`, `error_user`, `visual_user`, `performance_glitch_user`

### Products
- Product list display
- Sorting (Name and Price)
- Add / remove products from the list and details page

### Cart & Checkout
- Add and remove products
- Full checkout flow
- Form validation
- Empty cart checkout

### Negative & Special Users
- Logout
- Direct access to protected pages without login
- Behavior of special demo accounts

## Test Artifacts

| Artifact              | Description                     |
|-----------------------|---------------------------------|
| `test-cases/`         | 35 test cases by modules        |
| `bug-reports/bugs.md` | 15 bug reports                  |
| `checklists/`         | Smoke checklist                 |

## Test Execution Summary

| Metric              | Count |
|---------------------|-------|
| Total test cases    | 35    |
| Passed              | 22    |
| Failed              | 13    |
| Bugs found          | 15    |

## Key Findings

- Main user flow works correctly with `standard_user`
- High-severity issue: user can complete checkout with an empty cart
- Multiple functional and UI issues found with special demo users:
  - `problem_user` — broken images, sorting, form fields, product mismatch
  - `error_user` — sorting error, Last Name field not working
  - `visual_user` — layout issues, changing prices
  - `performance_glitch_user` — significant delays

## Tools

- Chrome / Safari
- Manual testing

## Notes

Sauce Demo is a training application. Special users are intentionally broken to help practice finding and reporting bugs.
