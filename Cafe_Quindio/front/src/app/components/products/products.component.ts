import { Component, OnInit } from '@angular/core';
import { ClientService } from '../../client.service';
import { FormGroup, FormBuilder, Validators } from '@angular/forms';
import { Router } from '@angular/router';
@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {
  form: FormGroup;
  constructor(private client: ClientService,     private fb: FormBuilder, private route: Router) { }
  // tslint:disable-next-line: variable-name
  list_product: [];
  // tslint:disable-next-line: variable-name
  id_fav: any;
  ngOnInit(): void {
  this.onSubmit(),
  this.form = this.fb.group({
    mobileline: ['', Validators.required],
    date: ['', Validators.required],
  });
  }

  async onSubmit() {
      this.client.getRequest('http://127.0.0.1:5000/api/v01/products',
      ).subscribe(

        (response: any) => {
          const { productos } = response;
          const [cafe1, cafe2] = productos;
          // tslint:disable-next-line: variable-name
          const [nombre, desc, price, id_c ] = cafe1;
          this.list_product = productos;
          this.id_fav = 'id_c';
          console.log(id_c);
      }),
      // tslint:disable-next-line: no-unused-expression
      (error) => {
        console.log(error.status);
      };
  }
  async addFav(i : any) {
    this.client.postRequest(`http://127.0.0.1:5000/api/v01/fav/${this.id_fav}`,{
    }
    ).subscribe(

      (response: any) => {
        console.log(response)
      }),
    // tslint:disable-next-line: no-unused-expression
    (error) => {
      console.log(error.status);
    };
}
  

}
