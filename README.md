# Welcome to Work Fit API
Oue API provides to user and admin_user to manage all included functionality. Project use Django DRF also for deploiment there is Docker and fort testing you can use Swagger. DB is Postgres.

## Work Fit API contains several applications
### Accounts
This application helps manage to register login and logout. This use JWT tokens.
#### Account end-points:
- api/accounts/register/ - need to add username and password and it registers user in db.
- api/accounts/login/ -  need to add username and password, you can login and returns JWT tocken
- api/accounts/logout/ -  you can logout

### Workouts
This application helps manage to add predefined workouts, add workouts can only admin users and view can all. 
#### Workouts end-points:
- api/workouts/workout/ - 