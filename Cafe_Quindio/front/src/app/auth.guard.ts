import { Injectable } from '@angular/core';
import { CanActivate, ActivatedRouteSnapshot, RouterStateSnapshot, UrlTree, Router } from '@angular/router';
import { Observable } from 'rxjs';
import { AuthService } from './auth.service';

@Injectable({
  providedIn: 'root'
})
export class AuthGuard implements CanActivate {
  constructor(private auth: AuthService, private route: Router){

  }
  canActivate(route: ActivatedRouteSnapshot, state: RouterStateSnapshot){
    if (!this.auth.isLogedIn) {
      this.route.navigate(['/'], { queryParams: { retUrl: route.url} });
      return false;
    }else{
      console.log('no estoy logeado' );
      return true;
    }
  }
}
