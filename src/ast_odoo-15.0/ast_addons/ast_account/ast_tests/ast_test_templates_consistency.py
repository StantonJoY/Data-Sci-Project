Module(
    body=[
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='TransactionCase', asname=None)],
            level=0,
        ),
        ClassDef(
            name='AccountingTestTemplConsistency',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Test the templates consistency between some objects like account.account when account.account.template.\n    ', kind=None),
                ),
                FunctionDef(
                    name='get_model_fields',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model', annotation=None, type_comment=None),
                            arg(arg='extra_domain', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='model', kind=None),
                                            Constant(value='=', kind=None),
                                            Name(id='model', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='state', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value='base', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='related', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='compute', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=False, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='store', kind=None),
                                            Constant(value='=', kind=None),
                                            Constant(value=True, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='extra_domain', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='domain', ctx=Store()),
                                    op=Add(),
                                    value=Name(id='extra_domain', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.model.fields', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='check_fields_consistency',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='model_from', annotation=None, type_comment=None),
                            arg(arg='model_to', annotation=None, type_comment=None),
                            arg(arg='exceptions', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Check the consistency of fields from one model to another by comparing if all fields\n        in the model_from are present in the model_to.\n        :param model_from: The model to compare.\n        :param model_to: The compared model.\n        :param exceptions: Not copied model's fields.\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='extra_domain', ctx=Store())],
                            value=IfExp(
                                test=Name(id='exceptions', ctx=Load()),
                                body=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='name', kind=None),
                                                Constant(value='not in', kind=None),
                                                Name(id='exceptions', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                                orelse=List(elts=[], ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='from_fields', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='get_model_fields',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='model_from', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='extra_domain',
                                                value=Name(id='extra_domain', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    attr='filtered_domain',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='modules', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Constant(value='account', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='to_fields_set', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    ListComp(
                                        elt=Attribute(
                                            value=Name(id='f', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='f', ctx=Store()),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='get_model_fields',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='model_to', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='field', ctx=Store()),
                            iter=Name(id='from_fields', ctx=Load()),
                            body=[
                                Assert(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='field', ctx=Load()),
                                            attr='name',
                                            ctx=Load(),
                                        ),
                                        ops=[In()],
                                        comparators=[Name(id='to_fields_set', ctx=Load())],
                                    ),
                                    msg=BinOp(
                                        left=Constant(value='Missing field "%s" from "%s" in model "%s".', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                Attribute(
                                                    value=Name(id='field', ctx=Load()),
                                                    attr='name',
                                                    ctx=Load(),
                                                ),
                                                Name(id='model_from', ctx=Load()),
                                                Name(id='model_to', ctx=Load()),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_account_account_fields',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Test fields consistency for ('account.account', 'account.account.template')\n        ", kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_fields_consistency',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account.account.template', kind=None),
                                    Constant(value='account.account', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='exceptions',
                                        value=List(
                                            elts=[
                                                Constant(value='chart_template_id', kind=None),
                                                Constant(value='nocreate', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_fields_consistency',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account.account', kind=None),
                                    Constant(value='account.account.template', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='exceptions',
                                        value=List(
                                            elts=[
                                                Constant(value='company_id', kind=None),
                                                Constant(value='deprecated', kind=None),
                                                Constant(value='opening_debit', kind=None),
                                                Constant(value='opening_credit', kind=None),
                                                Constant(value='allowed_journal_ids', kind=None),
                                                Constant(value='group_id', kind=None),
                                                Constant(value='root_id', kind=None),
                                                Constant(value='is_off_balance', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_account_tax_fields',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Test fields consistency for ('account.tax', 'account.tax.template')\n        ", kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_fields_consistency',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account.tax.template', kind=None),
                                    Constant(value='account.tax', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='exceptions',
                                        value=List(
                                            elts=[Constant(value='chart_template_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_fields_consistency',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account.tax', kind=None),
                                    Constant(value='account.tax.template', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='exceptions',
                                        value=List(
                                            elts=[
                                                Constant(value='company_id', kind=None),
                                                Constant(value='country_id', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_fields_consistency',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account.tax.repartition.line.template', kind=None),
                                    Constant(value='account.tax.repartition.line', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='exceptions',
                                        value=List(
                                            elts=[
                                                Constant(value='plus_report_line_ids', kind=None),
                                                Constant(value='minus_report_line_ids', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_fields_consistency',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account.tax.repartition.line', kind=None),
                                    Constant(value='account.tax.repartition.line.template', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='exceptions',
                                        value=List(
                                            elts=[
                                                Constant(value='tag_ids', kind=None),
                                                Constant(value='country_id', kind=None),
                                                Constant(value='company_id', kind=None),
                                                Constant(value='sequence', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_fiscal_position_fields',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Test fields consistency for ('account.fiscal.position', 'account.fiscal.position.template')\n        ", kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_fields_consistency',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account.fiscal.position.template', kind=None),
                                    Constant(value='account.fiscal.position', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='exceptions',
                                        value=List(
                                            elts=[Constant(value='chart_template_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_fields_consistency',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account.fiscal.position', kind=None),
                                    Constant(value='account.fiscal.position.template', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='exceptions',
                                        value=List(
                                            elts=[
                                                Constant(value='active', kind=None),
                                                Constant(value='company_id', kind=None),
                                                Constant(value='states_count', kind=None),
                                                Constant(value='foreign_vat', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_fields_consistency',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account.fiscal.position.tax.template', kind=None),
                                    Constant(value='account.fiscal.position.tax', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_fields_consistency',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account.fiscal.position.tax', kind=None),
                                    Constant(value='account.fiscal.position.tax.template', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_fields_consistency',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account.fiscal.position.account.template', kind=None),
                                    Constant(value='account.fiscal.position.account', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_fields_consistency',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account.fiscal.position.account', kind=None),
                                    Constant(value='account.fiscal.position.account.template', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_reconcile_model_fields',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Test fields consistency for ('account.reconcile.model', 'account.reconcile.model.template')\n        ", kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_fields_consistency',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account.reconcile.model.template', kind=None),
                                    Constant(value='account.reconcile.model', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='exceptions',
                                        value=List(
                                            elts=[Constant(value='chart_template_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='mail_thread_fields', ctx=Store())],
                            value=ListComp(
                                elt=Attribute(
                                    value=Name(id='field', ctx=Load()),
                                    attr='name',
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='field', ctx=Store()),
                                        iter=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='get_model_fields',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='mail.thread', kind=None)],
                                            keywords=[],
                                        ),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_fields_consistency',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account.reconcile.model', kind=None),
                                    Constant(value='account.reconcile.model.template', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='exceptions',
                                        value=BinOp(
                                            left=Name(id='mail_thread_fields', ctx=Load()),
                                            op=Add(),
                                            right=List(
                                                elts=[
                                                    Constant(value='active', kind=None),
                                                    Constant(value='company_id', kind=None),
                                                    Constant(value='past_months_limit', kind=None),
                                                    Constant(value='partner_mapping_line_ids', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_fields_consistency',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account.reconcile.model.line.template', kind=None),
                                    Constant(value='account.reconcile.model.line', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='exceptions',
                                        value=List(
                                            elts=[Constant(value='chart_template_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_fields_consistency',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account.reconcile.model.line', kind=None),
                                    Constant(value='account.reconcile.model.line.template', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='exceptions',
                                        value=List(
                                            elts=[
                                                Constant(value='company_id', kind=None),
                                                Constant(value='journal_id', kind=None),
                                                Constant(value='analytic_account_id', kind=None),
                                                Constant(value='analytic_tag_ids', kind=None),
                                                Constant(value='amount', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_account_group_fields',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value="Test fields consistency for ('account.group', 'account.group.template')\n        ", kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_fields_consistency',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account.group', kind=None),
                                    Constant(value='account.group.template', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='exceptions',
                                        value=List(
                                            elts=[
                                                Constant(value='company_id', kind=None),
                                                Constant(value='parent_path', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='check_fields_consistency',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='account.group.template', kind=None),
                                    Constant(value='account.group', kind=None),
                                ],
                                keywords=[
                                    keyword(
                                        arg='exceptions',
                                        value=List(
                                            elts=[Constant(value='chart_template_id', kind=None)],
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
