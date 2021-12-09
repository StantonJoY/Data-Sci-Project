Module(
    body=[
        Import(
            names=[alias(name='ast', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='datetime',
            names=[
                alias(name='date', asname=None),
                alias(name='datetime', asname=None),
                alias(name='timedelta', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='_', asname=None),
                alias(name='exceptions', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.osv',
            names=[alias(name='expression', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.safe_eval',
            names=[
                alias(name='safe_eval', asname=None),
                alias(name='time', asname=None),
            ],
            level=0,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DOMAIN_TEMPLATE', ctx=Store())],
            value=Constant(value="[('store', '=', True), '|', ('model_id', '=', model_id), ('model_id', 'in', model_inherited_ids)%s]", kind=None),
            type_comment=None,
        ),
        ClassDef(
            name='GoalDefinition',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Goal definition\n\n    A goal definition contains the way to evaluate an objective\n    Each module wanting to be able to set goals to the users needs to create\n    a new gamification_goal_definition\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='gamification.goal.definition', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Gamification Goal Definition', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Goal Definition', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='translate',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='description', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Goal Description', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='monetary', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Monetary Value', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The target and current value are defined in the company currency.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='suffix', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Suffix', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='The unit of the target and current values', kind=None),
                            ),
                            keyword(
                                arg='translate',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='full_suffix', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Full Suffix', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_full_suffix', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The currency and suffix field', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='computation_mode', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='manually', kind=None),
                                            Constant(value='Recorded manually', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='count', kind=None),
                                            Constant(value='Automatic: number of records', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='sum', kind=None),
                                            Constant(value='Automatic: sum on a field', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='python', kind=None),
                                            Constant(value='Automatic: execute a specific Python code', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='manually', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Computation Mode', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="Define how the goals will be computed. The result of the operation will be stored in the field 'Current'.", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='display_mode', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='progress', kind=None),
                                            Constant(value='Progressive (using numerical values)', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='boolean', kind=None),
                                            Constant(value='Exclusive (done or not-done)', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='progress', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Displayed as', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='model_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ir.model', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Model', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The model object for the field to evaluate', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='model_inherited_ids', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2many',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ir.model', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='model_id.inherited_model_ids', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='field_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ir.model.fields', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Field to Sum', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The field containing the value to evaluate', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=BinOp(
                                    left=Name(id='DOMAIN_TEMPLATE', ctx=Load()),
                                    op=Mod(),
                                    right=Constant(value='', kind=None),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='field_date_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ir.model.fields', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Date Field', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The date to use for the time period evaluated', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=BinOp(
                                    left=Name(id='DOMAIN_TEMPLATE', ctx=Load()),
                                    op=Mod(),
                                    right=Constant(value=", ('ttype', 'in', ('date', 'datetime'))", kind=None),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='domain', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Filter Domain', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='[]', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="Domain for filtering records. General rule, not user depending, e.g. [('state', '=', 'done')]. The expression can contain reference to 'user' which is a browse record of the current user if not in batch mode.", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='batch_mode', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Batch Mode', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Evaluate the expression in batch instead of once for each user', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='batch_distinctive_field', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ir.model.fields', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Distinctive field for batch user', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='In batch mode, this indicates which field distinguishes one user from the other, e.g. user_id, partner_id...', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='batch_user_expression', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Evaluated expression for batch mode', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value="The value to compare with the distinctive field. The expression can contain reference to 'user' which is a browse record of the current user, e.g. user.id, user.partner_id.id...", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='compute_code', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Python Code', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value="Python code to be executed for each user. 'result' should contains the new current value. Evaluated user can be access through object.user_id.", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='condition', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='higher', kind=None),
                                            Constant(value='The higher the better', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='lower', kind=None),
                                            Constant(value='The lower the better', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='higher', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Goal Performance', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='A goal is considered as completed when the current value is compared to the value to reach', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='action_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ir.actions.act_window', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Action', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The action that will be called to update the goal value.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='res_id_field', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='ID Field of user', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='The field name on the user profile (res.users) containing the value for res_id for action.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_full_suffix',
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
                        For(
                            target=Name(id='goal', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='items', ctx=Store())],
                                    value=List(elts=[], ctx=Load()),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='goal', ctx=Load()),
                                        attr='monetary',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='items', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            Attribute(
                                                                value=Attribute(
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='company',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='currency_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='symbol',
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='¤', kind='u'),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='goal', ctx=Load()),
                                        attr='suffix',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='items', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='goal', ctx=Load()),
                                                        attr='suffix',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='goal', ctx=Load()),
                                            attr='full_suffix',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Constant(value=' ', kind='u'),
                                            attr='join',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='items', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='suffix', kind=None),
                                Constant(value='monetary', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_domain_validity',
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
                        For(
                            target=Name(id='definition', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='definition', ctx=Load()),
                                            attr='computation_mode',
                                            ctx=Load(),
                                        ),
                                        ops=[NotIn()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='count', kind=None),
                                                    Constant(value='sum', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='Obj', ctx=Store())],
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Attribute(
                                            value=Attribute(
                                                value=Name(id='definition', ctx=Load()),
                                                attr='model_id',
                                                ctx=Load(),
                                            ),
                                            attr='model',
                                            ctx=Load(),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='domain', ctx=Store())],
                                            value=Call(
                                                func=Name(id='safe_eval', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='definition', ctx=Load()),
                                                        attr='domain',
                                                        ctx=Load(),
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='user', kind=None)],
                                                        values=[
                                                            Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='user',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='with_user',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='self', ctx=Load()),
                                                                            attr='env',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='user',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='Obj', ctx=Load()),
                                                    attr='search_count',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='domain', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Tuple(
                                                elts=[
                                                    Name(id='ValueError', ctx=Load()),
                                                    Name(id='SyntaxError', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            name='e',
                                            body=[
                                                Assign(
                                                    targets=[Name(id='msg', ctx=Store())],
                                                    value=Name(id='e', ctx=Load()),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Call(
                                                        func=Name(id='isinstance', ctx=Load()),
                                                        args=[
                                                            Name(id='e', ctx=Load()),
                                                            Name(id='SyntaxError', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='msg', ctx=Store())],
                                                            value=BinOp(
                                                                left=BinOp(
                                                                    left=Attribute(
                                                                        value=Name(id='e', ctx=Load()),
                                                                        attr='msg',
                                                                        ctx=Load(),
                                                                    ),
                                                                    op=Add(),
                                                                    right=Constant(value='\n', kind=None),
                                                                ),
                                                                op=Add(),
                                                                right=Attribute(
                                                                    value=Name(id='e', ctx=Load()),
                                                                    attr='text',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Raise(
                                                    exc=Call(
                                                        func=Attribute(
                                                            value=Name(id='exceptions', ctx=Load()),
                                                            attr='UserError',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            BinOp(
                                                                left=Call(
                                                                    func=Name(id='_', ctx=Load()),
                                                                    args=[Constant(value='The domain for the definition %s seems incorrect, please check it.\n\n%s', kind=None)],
                                                                    keywords=[],
                                                                ),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Attribute(
                                                                            value=Name(id='definition', ctx=Load()),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Name(id='msg', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_model_validity',
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
                            value=Constant(value=' make sure the selected field and model are usable', kind=None),
                        ),
                        For(
                            target=Name(id='definition', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Attribute(
                                                            value=Name(id='definition', ctx=Load()),
                                                            attr='model_id',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='definition', ctx=Load()),
                                                            attr='field_id',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Assign(
                                            targets=[Name(id='Model', ctx=Store())],
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='definition', ctx=Load()),
                                                        attr='model_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='model',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='field', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='Model', ctx=Load()),
                                                        attr='_fields',
                                                        ctx=Load(),
                                                    ),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='definition', ctx=Load()),
                                                            attr='field_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=BoolOp(
                                                    op=And(),
                                                    values=[
                                                        Name(id='field', ctx=Load()),
                                                        Attribute(
                                                            value=Name(id='field', ctx=Load()),
                                                            attr='store',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                ),
                                            ),
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Attribute(
                                                            value=Name(id='exceptions', ctx=Load()),
                                                            attr='UserError',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='The model configuration for the definition %(name)s seems incorrect, please check it.\n\n%(field_name)s not stored', kind=None)],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='name',
                                                                        value=Attribute(
                                                                            value=Name(id='definition', ctx=Load()),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='field_name',
                                                                        value=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='definition', ctx=Load()),
                                                                                attr='field_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='KeyError', ctx=Load()),
                                            name='e',
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Attribute(
                                                            value=Name(id='exceptions', ctx=Load()),
                                                            attr='UserError',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='The model configuration for the definition %(name)s seems incorrect, please check it.\n\n%(error)s not found', kind=None)],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='name',
                                                                        value=Attribute(
                                                                            value=Name(id='definition', ctx=Load()),
                                                                            attr='name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    keyword(
                                                                        arg='error',
                                                                        value=Name(id='e', ctx=Load()),
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    cause=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
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
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='definitions', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='GoalDefinition', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals_list', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='definitions', ctx=Load()),
                                            attr='filtered_domain',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='computation_mode', kind=None),
                                                            Constant(value='in', kind=None),
                                                            List(
                                                                elts=[
                                                                    Constant(value='count', kind=None),
                                                                    Constant(value='sum', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_check_domain_validity',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='definitions', ctx=Load()),
                                            attr='filtered_domain',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='field_id', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Constant(value='True', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_check_model_validity',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Name(id='definitions', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model_create_multi',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='GoalDefinition', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Compare(
                                        left=Call(
                                            func=Attribute(
                                                value=Name(id='vals', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='computation_mode', kind=None),
                                                Constant(value='count', kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[In()],
                                        comparators=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='count', kind=None),
                                                    Constant(value='sum', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='vals', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='domain', kind=None)],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='vals', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='model_id', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_check_domain_validity',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='field_id', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='model_id', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='vals', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='batch_mode', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_check_model_validity',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='Goal',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value='Goal instance for a user\n\n    An individual goal for a user on a specified time period', kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='gamification.goal', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Gamification Goal', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_rec_name', ctx=Store())],
                    value=Constant(value='definition_id', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='start_date desc, end_date desc, definition_id, id', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='definition_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='gamification.goal.definition', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Goal Definition', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='user_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='res.users', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='User', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='auto_join',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='line_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[Constant(value='gamification.challenge.line', kind=None)],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Challenge Line', kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='challenge_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='line_id.challenge_id', kind=None),
                            ),
                            keyword(
                                arg='store',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='index',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Challenge that generated the goal, assign challenge to users to generate goals with a value in this field.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='start_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Start Date', kind=None)],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Date',
                                        ctx=Load(),
                                    ),
                                    attr='today',
                                    ctx=Load(),
                                ),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='end_date', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[Constant(value='End Date', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='target_goal', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='To Reach', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='current', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Current Value', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value=0, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='completeness', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Float',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Completeness', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_get_completion', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='state', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='draft', kind=None),
                                            Constant(value='Draft', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='inprogress', kind=None),
                                            Constant(value='In progress', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='reached', kind=None),
                                            Constant(value='Reached', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='failed', kind=None),
                                            Constant(value='Failed', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='canceled', kind=None),
                                            Constant(value='Canceled', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Constant(value='draft', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='State', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='to_update', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='To update', kind=None)],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='closed', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Closed goal', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='These goals will not be recomputed.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='computation_mode', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='definition_id.computation_mode', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='remind_update_delay', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Remind delay', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='The number of days after which the user assigned to a manual goal will be reminded. Never reminded if no value is specified.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='last_update', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Date',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Last Update', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='In case of manual goal, reminders are sent if the goal as not been updated for a while (defined in challenge). Ignored in case of non-manual goal or goal not linked to a challenge.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='definition_description', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Definition Description', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='definition_id.description', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='definition_condition', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Definition Condition', kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='definition_id.condition', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='definition_suffix', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Suffix', kind=None)],
                        keywords=[
                            keyword(
                                arg='related',
                                value=Constant(value='definition_id.full_suffix', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='definition_display', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Display Mode', kind=None),
                            ),
                            keyword(
                                arg='related',
                                value=Constant(value='definition_id.display_mode', kind=None),
                            ),
                            keyword(
                                arg='readonly',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_completion',
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
                            value=Constant(value='Return the percentage of completeness of the goal, between 0 and 100', kind=None),
                        ),
                        For(
                            target=Name(id='goal', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='goal', ctx=Load()),
                                            attr='definition_condition',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='higher', kind=None)],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='goal', ctx=Load()),
                                                    attr='current',
                                                    ctx=Load(),
                                                ),
                                                ops=[GtE()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='goal', ctx=Load()),
                                                        attr='target_goal',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='goal', ctx=Load()),
                                                            attr='completeness',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=100.0, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='goal', ctx=Load()),
                                                            attr='completeness',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=IfExp(
                                                        test=Attribute(
                                                            value=Name(id='goal', ctx=Load()),
                                                            attr='target_goal',
                                                            ctx=Load(),
                                                        ),
                                                        body=Call(
                                                            func=Name(id='round', ctx=Load()),
                                                            args=[
                                                                BinOp(
                                                                    left=BinOp(
                                                                        left=Constant(value=100.0, kind=None),
                                                                        op=Mult(),
                                                                        right=Attribute(
                                                                            value=Name(id='goal', ctx=Load()),
                                                                            attr='current',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    op=Div(),
                                                                    right=Attribute(
                                                                        value=Name(id='goal', ctx=Load()),
                                                                        attr='target_goal',
                                                                        ctx=Load(),
                                                                    ),
                                                                ),
                                                                Constant(value=2, kind=None),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        orelse=Constant(value=0, kind=None),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='goal', ctx=Load()),
                                                    attr='current',
                                                    ctx=Load(),
                                                ),
                                                ops=[Lt()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='goal', ctx=Load()),
                                                        attr='target_goal',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='goal', ctx=Load()),
                                                            attr='completeness',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=100.0, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Attribute(
                                                            value=Name(id='goal', ctx=Load()),
                                                            attr='completeness',
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Constant(value=0.0, kind=None),
                                                    type_comment=None,
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='depends',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='current', kind=None),
                                Constant(value='target_goal', kind=None),
                                Constant(value='definition_id.condition', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_remind_delay',
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
                            value=Constant(value='Verify if a goal has not been updated for some time and send a\n        reminder message of needed.\n\n        :return: data to write on the goal object\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=BoolOp(
                                    op=And(),
                                    values=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='remind_update_delay',
                                            ctx=Load(),
                                        ),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='last_update',
                                            ctx=Load(),
                                        ),
                                    ],
                                ),
                            ),
                            body=[
                                Return(
                                    value=Dict(keys=[], values=[]),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='delta_max', ctx=Store())],
                            value=Call(
                                func=Name(id='timedelta', ctx=Load()),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='days',
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='remind_update_delay',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='last_update', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Date',
                                        ctx=Load(),
                                    ),
                                    attr='from_string',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='last_update',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=BinOp(
                                    left=Call(
                                        func=Attribute(
                                            value=Name(id='date', ctx=Load()),
                                            attr='today',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    op=Sub(),
                                    right=Name(id='last_update', ctx=Load()),
                                ),
                                ops=[Lt()],
                                comparators=[Name(id='delta_max', ctx=Load())],
                            ),
                            body=[
                                Return(
                                    value=Dict(keys=[], values=[]),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='body_html', ctx=Store())],
                            value=Subscript(
                                value=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='ref',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='gamification.email_template_goal_reminder', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='_render_field',
                                        ctx=Load(),
                                    ),
                                    args=[
                                        Constant(value='body_html', kind=None),
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[
                                        keyword(
                                            arg='compute_lang',
                                            value=Constant(value=True, kind=None),
                                        ),
                                    ],
                                ),
                                slice=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='id',
                                    ctx=Load(),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='message_notify',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='body',
                                        value=Name(id='body_html', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='partner_ids',
                                        value=List(
                                            elts=[
                                                Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='user_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    keyword(
                                        arg='subtype_xmlid',
                                        value=Constant(value='mail.mt_comment', kind=None),
                                    ),
                                    keyword(
                                        arg='email_layout_xmlid',
                                        value=Constant(value='mail.mail_notification_light', kind=None),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Dict(
                                keys=[Constant(value='to_update', kind=None)],
                                values=[Constant(value=True, kind=None)],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_write_values',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='new_value', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Generate values to write after recomputation of a goal score', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Name(id='new_value', ctx=Load()),
                                ops=[Eq()],
                                comparators=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='current',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Dict(keys=[], values=[]),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='current', kind=None)],
                                values=[Name(id='new_value', ctx=Load())],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='definition_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='condition',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='higher', kind=None)],
                                            ),
                                            Compare(
                                                left=Name(id='new_value', ctx=Load()),
                                                ops=[GtE()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='target_goal',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='definition_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='condition',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='lower', kind=None)],
                                            ),
                                            Compare(
                                                left=Name(id='new_value', ctx=Load()),
                                                ops=[LtE()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='target_goal',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='result', ctx=Load()),
                                            slice=Constant(value='state', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value='reached', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='end_date',
                                                ctx=Load(),
                                            ),
                                            Compare(
                                                left=Call(
                                                    func=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='fields', ctx=Load()),
                                                            attr='Date',
                                                            ctx=Load(),
                                                        ),
                                                        attr='today',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ops=[Gt()],
                                                comparators=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='end_date',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='result', ctx=Load()),
                                                    slice=Constant(value='state', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='failed', kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='result', ctx=Load()),
                                                    slice=Constant(value='closed', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                        ),
                        Return(
                            value=Dict(
                                keys=[Name(id='self', ctx=Load())],
                                values=[Name(id='result', ctx=Load())],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='update_goal',
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
                            value=Constant(value="Update the goals to recomputes values and change of states\n\n        If a manual goal is not updated for enough time, the user will be\n        reminded to do so (done only once, in 'inprogress' state).\n        If a goal reaches the target value, the status is set to reached\n        If the end date is passed (at least +1 day, time not considered) without\n        the target value being reached, the goal is set as failed.", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='goals_by_definition', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='goal', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='with_context',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='prefetch_fields',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='goals_by_definition', ctx=Load()),
                                                    attr='setdefault',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='goal', ctx=Load()),
                                                        attr='definition_id',
                                                        ctx=Load(),
                                                    ),
                                                    List(elts=[], ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='goal', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='definition', ctx=Store()),
                                    Name(id='goals', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='goals_by_definition', ctx=Load()),
                                    attr='items',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='goals_to_write', ctx=Store())],
                                    value=Dict(keys=[], values=[]),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Attribute(
                                            value=Name(id='definition', ctx=Load()),
                                            attr='computation_mode',
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value='manually', kind=None)],
                                    ),
                                    body=[
                                        For(
                                            target=Name(id='goal', ctx=Store()),
                                            iter=Name(id='goals', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='goals_to_write', ctx=Load()),
                                                            slice=Name(id='goal', ctx=Load()),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='goal', ctx=Load()),
                                                            attr='_check_remind_delay',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Name(id='definition', ctx=Load()),
                                                    attr='computation_mode',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='python', kind=None)],
                                            ),
                                            body=[
                                                For(
                                                    target=Name(id='goal', ctx=Store()),
                                                    iter=Name(id='goals', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='cxt', ctx=Store())],
                                                            value=Dict(
                                                                keys=[
                                                                    Constant(value='object', kind=None),
                                                                    Constant(value='env', kind=None),
                                                                    Constant(value='date', kind=None),
                                                                    Constant(value='datetime', kind=None),
                                                                    Constant(value='timedelta', kind=None),
                                                                    Constant(value='time', kind=None),
                                                                ],
                                                                values=[
                                                                    Name(id='goal', ctx=Load()),
                                                                    Attribute(
                                                                        value=Name(id='self', ctx=Load()),
                                                                        attr='env',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Name(id='date', ctx=Load()),
                                                                    Name(id='datetime', ctx=Load()),
                                                                    Name(id='timedelta', ctx=Load()),
                                                                    Name(id='time', ctx=Load()),
                                                                ],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='code', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='definition', ctx=Load()),
                                                                        attr='compute_code',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='strip',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Expr(
                                                            value=Call(
                                                                func=Name(id='safe_eval', ctx=Load()),
                                                                args=[
                                                                    Name(id='code', ctx=Load()),
                                                                    Name(id='cxt', ctx=Load()),
                                                                ],
                                                                keywords=[
                                                                    keyword(
                                                                        arg='mode',
                                                                        value=Constant(value='exec', kind=None),
                                                                    ),
                                                                    keyword(
                                                                        arg='nocopy',
                                                                        value=Constant(value=True, kind=None),
                                                                    ),
                                                                ],
                                                            ),
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='result', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='cxt', ctx=Load()),
                                                                    attr='get',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value='result', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Call(
                                                                func=Name(id='isinstance', ctx=Load()),
                                                                args=[
                                                                    Name(id='result', ctx=Load()),
                                                                    Tuple(
                                                                        elts=[
                                                                            Name(id='float', ctx=Load()),
                                                                            Name(id='int', ctx=Load()),
                                                                        ],
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='goals_to_write', ctx=Load()),
                                                                            attr='update',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='goal', ctx=Load()),
                                                                                    attr='_get_write_values',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='result', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='_logger', ctx=Load()),
                                                                            attr='error',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Constant(value="Invalid return content '%r' from the evaluation of code for definition %s, expected a number", kind=None),
                                                                            Name(id='result', ctx=Load()),
                                                                            Attribute(
                                                                                value=Name(id='definition', ctx=Load()),
                                                                                attr='name',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='definition', ctx=Load()),
                                                            attr='computation_mode',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[In()],
                                                        comparators=[
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='count', kind=None),
                                                                    Constant(value='sum', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='Obj', ctx=Store())],
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='definition', ctx=Load()),
                                                                        attr='model_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='model',
                                                                    ctx=Load(),
                                                                ),
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='field_date_name', ctx=Store())],
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='definition', ctx=Load()),
                                                                    attr='field_date_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='name',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=Attribute(
                                                                value=Name(id='definition', ctx=Load()),
                                                                attr='batch_mode',
                                                                ctx=Load(),
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='general_domain', ctx=Store())],
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='ast', ctx=Load()),
                                                                            attr='literal_eval',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Attribute(
                                                                                value=Name(id='definition', ctx=Load()),
                                                                                attr='domain',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='field_name', ctx=Store())],
                                                                    value=Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='definition', ctx=Load()),
                                                                            attr='batch_distinctive_field',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='subqueries', ctx=Store())],
                                                                    value=Dict(keys=[], values=[]),
                                                                    type_comment=None,
                                                                ),
                                                                For(
                                                                    target=Name(id='goal', ctx=Store()),
                                                                    iter=Name(id='goals', ctx=Load()),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='start_date', ctx=Store())],
                                                                            value=BoolOp(
                                                                                op=Or(),
                                                                                values=[
                                                                                    BoolOp(
                                                                                        op=And(),
                                                                                        values=[
                                                                                            Name(id='field_date_name', ctx=Load()),
                                                                                            Attribute(
                                                                                                value=Name(id='goal', ctx=Load()),
                                                                                                attr='start_date',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    Constant(value=False, kind=None),
                                                                                ],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        Assign(
                                                                            targets=[Name(id='end_date', ctx=Store())],
                                                                            value=BoolOp(
                                                                                op=Or(),
                                                                                values=[
                                                                                    BoolOp(
                                                                                        op=And(),
                                                                                        values=[
                                                                                            Name(id='field_date_name', ctx=Load()),
                                                                                            Attribute(
                                                                                                value=Name(id='goal', ctx=Load()),
                                                                                                attr='end_date',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    Constant(value=False, kind=None),
                                                                                ],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='subqueries', ctx=Load()),
                                                                                            attr='setdefault',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Tuple(
                                                                                                elts=[
                                                                                                    Name(id='start_date', ctx=Load()),
                                                                                                    Name(id='end_date', ctx=Load()),
                                                                                                ],
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            Dict(keys=[], values=[]),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    attr='update',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Dict(
                                                                                        keys=[
                                                                                            Attribute(
                                                                                                value=Name(id='goal', ctx=Load()),
                                                                                                attr='id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        values=[
                                                                                            Call(
                                                                                                func=Name(id='safe_eval', ctx=Load()),
                                                                                                args=[
                                                                                                    Attribute(
                                                                                                        value=Name(id='definition', ctx=Load()),
                                                                                                        attr='batch_user_expression',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    Dict(
                                                                                                        keys=[Constant(value='user', kind=None)],
                                                                                                        values=[
                                                                                                            Attribute(
                                                                                                                value=Name(id='goal', ctx=Load()),
                                                                                                                attr='user_id',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                ],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                    type_comment=None,
                                                                ),
                                                                For(
                                                                    target=Tuple(
                                                                        elts=[
                                                                            Tuple(
                                                                                elts=[
                                                                                    Name(id='start_date', ctx=Store()),
                                                                                    Name(id='end_date', ctx=Store()),
                                                                                ],
                                                                                ctx=Store(),
                                                                            ),
                                                                            Name(id='query_goals', ctx=Store()),
                                                                        ],
                                                                        ctx=Store(),
                                                                    ),
                                                                    iter=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='subqueries', ctx=Load()),
                                                                            attr='items',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='subquery_domain', ctx=Store())],
                                                                            value=Call(
                                                                                func=Name(id='list', ctx=Load()),
                                                                                args=[Name(id='general_domain', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='subquery_domain', ctx=Load()),
                                                                                    attr='append',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Tuple(
                                                                                        elts=[
                                                                                            Name(id='field_name', ctx=Load()),
                                                                                            Constant(value='in', kind=None),
                                                                                            Call(
                                                                                                func=Name(id='list', ctx=Load()),
                                                                                                args=[
                                                                                                    Call(
                                                                                                        func=Name(id='set', ctx=Load()),
                                                                                                        args=[
                                                                                                            Call(
                                                                                                                func=Attribute(
                                                                                                                    value=Name(id='query_goals', ctx=Load()),
                                                                                                                    attr='values',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                args=[],
                                                                                                                keywords=[],
                                                                                                            ),
                                                                                                        ],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                ],
                                                                                                keywords=[],
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                        If(
                                                                            test=Name(id='start_date', ctx=Load()),
                                                                            body=[
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='subquery_domain', ctx=Load()),
                                                                                            attr='append',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Tuple(
                                                                                                elts=[
                                                                                                    Name(id='field_date_name', ctx=Load()),
                                                                                                    Constant(value='>=', kind=None),
                                                                                                    Name(id='start_date', ctx=Load()),
                                                                                                ],
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            orelse=[],
                                                                        ),
                                                                        If(
                                                                            test=Name(id='end_date', ctx=Load()),
                                                                            body=[
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='subquery_domain', ctx=Load()),
                                                                                            attr='append',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Tuple(
                                                                                                elts=[
                                                                                                    Name(id='field_date_name', ctx=Load()),
                                                                                                    Constant(value='<=', kind=None),
                                                                                                    Name(id='end_date', ctx=Load()),
                                                                                                ],
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            orelse=[],
                                                                        ),
                                                                        If(
                                                                            test=Compare(
                                                                                left=Attribute(
                                                                                    value=Name(id='definition', ctx=Load()),
                                                                                    attr='computation_mode',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='count', kind=None)],
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='value_field_name', ctx=Store())],
                                                                                    value=BinOp(
                                                                                        left=Name(id='field_name', ctx=Load()),
                                                                                        op=Add(),
                                                                                        right=Constant(value='_count', kind=None),
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                                If(
                                                                                    test=Compare(
                                                                                        left=Name(id='field_name', ctx=Load()),
                                                                                        ops=[Eq()],
                                                                                        comparators=[Constant(value='id', kind=None)],
                                                                                    ),
                                                                                    body=[
                                                                                        Assign(
                                                                                            targets=[Name(id='users', ctx=Store())],
                                                                                            value=Call(
                                                                                                func=Attribute(
                                                                                                    value=Name(id='Obj', ctx=Load()),
                                                                                                    attr='search',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[Name(id='subquery_domain', ctx=Load())],
                                                                                                keywords=[],
                                                                                            ),
                                                                                            type_comment=None,
                                                                                        ),
                                                                                        Assign(
                                                                                            targets=[Name(id='user_values', ctx=Store())],
                                                                                            value=ListComp(
                                                                                                elt=Dict(
                                                                                                    keys=[
                                                                                                        Constant(value='id', kind=None),
                                                                                                        Name(id='value_field_name', ctx=Load()),
                                                                                                    ],
                                                                                                    values=[
                                                                                                        Attribute(
                                                                                                            value=Name(id='user', ctx=Load()),
                                                                                                            attr='id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        Constant(value=1, kind=None),
                                                                                                    ],
                                                                                                ),
                                                                                                generators=[
                                                                                                    comprehension(
                                                                                                        target=Name(id='user', ctx=Store()),
                                                                                                        iter=Name(id='users', ctx=Load()),
                                                                                                        ifs=[],
                                                                                                        is_async=0,
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            type_comment=None,
                                                                                        ),
                                                                                    ],
                                                                                    orelse=[
                                                                                        Assign(
                                                                                            targets=[Name(id='user_values', ctx=Store())],
                                                                                            value=Call(
                                                                                                func=Attribute(
                                                                                                    value=Name(id='Obj', ctx=Load()),
                                                                                                    attr='read_group',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[Name(id='subquery_domain', ctx=Load())],
                                                                                                keywords=[
                                                                                                    keyword(
                                                                                                        arg='fields',
                                                                                                        value=List(
                                                                                                            elts=[Name(id='field_name', ctx=Load())],
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                    ),
                                                                                                    keyword(
                                                                                                        arg='groupby',
                                                                                                        value=List(
                                                                                                            elts=[Name(id='field_name', ctx=Load())],
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            type_comment=None,
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                Assign(
                                                                                    targets=[Name(id='value_field_name', ctx=Store())],
                                                                                    value=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='definition', ctx=Load()),
                                                                                            attr='field_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='name',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                                If(
                                                                                    test=Compare(
                                                                                        left=Name(id='field_name', ctx=Load()),
                                                                                        ops=[Eq()],
                                                                                        comparators=[Constant(value='id', kind=None)],
                                                                                    ),
                                                                                    body=[
                                                                                        Assign(
                                                                                            targets=[Name(id='user_values', ctx=Store())],
                                                                                            value=Call(
                                                                                                func=Attribute(
                                                                                                    value=Name(id='Obj', ctx=Load()),
                                                                                                    attr='search_read',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[Name(id='subquery_domain', ctx=Load())],
                                                                                                keywords=[
                                                                                                    keyword(
                                                                                                        arg='fields',
                                                                                                        value=List(
                                                                                                            elts=[
                                                                                                                Constant(value='id', kind=None),
                                                                                                                Name(id='value_field_name', ctx=Load()),
                                                                                                            ],
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            type_comment=None,
                                                                                        ),
                                                                                    ],
                                                                                    orelse=[
                                                                                        Assign(
                                                                                            targets=[Name(id='user_values', ctx=Store())],
                                                                                            value=Call(
                                                                                                func=Attribute(
                                                                                                    value=Name(id='Obj', ctx=Load()),
                                                                                                    attr='read_group',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                args=[Name(id='subquery_domain', ctx=Load())],
                                                                                                keywords=[
                                                                                                    keyword(
                                                                                                        arg='fields',
                                                                                                        value=List(
                                                                                                            elts=[
                                                                                                                Name(id='field_name', ctx=Load()),
                                                                                                                BinOp(
                                                                                                                    left=Constant(value='%s:sum', kind=None),
                                                                                                                    op=Mod(),
                                                                                                                    right=Name(id='value_field_name', ctx=Load()),
                                                                                                                ),
                                                                                                            ],
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                    ),
                                                                                                    keyword(
                                                                                                        arg='groupby',
                                                                                                        value=List(
                                                                                                            elts=[Name(id='field_name', ctx=Load())],
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            type_comment=None,
                                                                                        ),
                                                                                    ],
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        For(
                                                                            target=Name(id='goal', ctx=Store()),
                                                                            iter=ListComp(
                                                                                elt=Name(id='g', ctx=Load()),
                                                                                generators=[
                                                                                    comprehension(
                                                                                        target=Name(id='g', ctx=Store()),
                                                                                        iter=Name(id='goals', ctx=Load()),
                                                                                        ifs=[
                                                                                            Compare(
                                                                                                left=Attribute(
                                                                                                    value=Name(id='g', ctx=Load()),
                                                                                                    attr='id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[In()],
                                                                                                comparators=[Name(id='query_goals', ctx=Load())],
                                                                                            ),
                                                                                        ],
                                                                                        is_async=0,
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                For(
                                                                                    target=Name(id='user_value', ctx=Store()),
                                                                                    iter=Name(id='user_values', ctx=Load()),
                                                                                    body=[
                                                                                        Assign(
                                                                                            targets=[Name(id='queried_value', ctx=Store())],
                                                                                            value=BoolOp(
                                                                                                op=Or(),
                                                                                                values=[
                                                                                                    BoolOp(
                                                                                                        op=And(),
                                                                                                        values=[
                                                                                                            Compare(
                                                                                                                left=Name(id='field_name', ctx=Load()),
                                                                                                                ops=[In()],
                                                                                                                comparators=[Name(id='user_value', ctx=Load())],
                                                                                                            ),
                                                                                                            Subscript(
                                                                                                                value=Name(id='user_value', ctx=Load()),
                                                                                                                slice=Name(id='field_name', ctx=Load()),
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                    ),
                                                                                                    Constant(value=False, kind=None),
                                                                                                ],
                                                                                            ),
                                                                                            type_comment=None,
                                                                                        ),
                                                                                        If(
                                                                                            test=BoolOp(
                                                                                                op=And(),
                                                                                                values=[
                                                                                                    Call(
                                                                                                        func=Name(id='isinstance', ctx=Load()),
                                                                                                        args=[
                                                                                                            Name(id='queried_value', ctx=Load()),
                                                                                                            Name(id='tuple', ctx=Load()),
                                                                                                        ],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                    Compare(
                                                                                                        left=Call(
                                                                                                            func=Name(id='len', ctx=Load()),
                                                                                                            args=[Name(id='queried_value', ctx=Load())],
                                                                                                            keywords=[],
                                                                                                        ),
                                                                                                        ops=[Eq()],
                                                                                                        comparators=[Constant(value=2, kind=None)],
                                                                                                    ),
                                                                                                    Call(
                                                                                                        func=Name(id='isinstance', ctx=Load()),
                                                                                                        args=[
                                                                                                            Subscript(
                                                                                                                value=Name(id='queried_value', ctx=Load()),
                                                                                                                slice=Constant(value=0, kind=None),
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                            Name(id='int', ctx=Load()),
                                                                                                        ],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            body=[
                                                                                                Assign(
                                                                                                    targets=[Name(id='queried_value', ctx=Store())],
                                                                                                    value=Subscript(
                                                                                                        value=Name(id='queried_value', ctx=Load()),
                                                                                                        slice=Constant(value=0, kind=None),
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    type_comment=None,
                                                                                                ),
                                                                                            ],
                                                                                            orelse=[],
                                                                                        ),
                                                                                        If(
                                                                                            test=Compare(
                                                                                                left=Name(id='queried_value', ctx=Load()),
                                                                                                ops=[Eq()],
                                                                                                comparators=[
                                                                                                    Subscript(
                                                                                                        value=Name(id='query_goals', ctx=Load()),
                                                                                                        slice=Attribute(
                                                                                                            value=Name(id='goal', ctx=Load()),
                                                                                                            attr='id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            body=[
                                                                                                Assign(
                                                                                                    targets=[Name(id='new_value', ctx=Store())],
                                                                                                    value=Call(
                                                                                                        func=Attribute(
                                                                                                            value=Name(id='user_value', ctx=Load()),
                                                                                                            attr='get',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        args=[
                                                                                                            Name(id='value_field_name', ctx=Load()),
                                                                                                            Attribute(
                                                                                                                value=Name(id='goal', ctx=Load()),
                                                                                                                attr='current',
                                                                                                                ctx=Load(),
                                                                                                            ),
                                                                                                        ],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                    type_comment=None,
                                                                                                ),
                                                                                                Expr(
                                                                                                    value=Call(
                                                                                                        func=Attribute(
                                                                                                            value=Name(id='goals_to_write', ctx=Load()),
                                                                                                            attr='update',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        args=[
                                                                                                            Call(
                                                                                                                func=Attribute(
                                                                                                                    value=Name(id='goal', ctx=Load()),
                                                                                                                    attr='_get_write_values',
                                                                                                                    ctx=Load(),
                                                                                                                ),
                                                                                                                args=[Name(id='new_value', ctx=Load())],
                                                                                                                keywords=[],
                                                                                                            ),
                                                                                                        ],
                                                                                                        keywords=[],
                                                                                                    ),
                                                                                                ),
                                                                                            ],
                                                                                            orelse=[],
                                                                                        ),
                                                                                    ],
                                                                                    orelse=[],
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                            orelse=[],
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                For(
                                                                    target=Name(id='goal', ctx=Store()),
                                                                    iter=Name(id='goals', ctx=Load()),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='domain', ctx=Store())],
                                                                            value=Call(
                                                                                func=Name(id='safe_eval', ctx=Load()),
                                                                                args=[
                                                                                    Attribute(
                                                                                        value=Name(id='definition', ctx=Load()),
                                                                                        attr='domain',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Dict(
                                                                                        keys=[Constant(value='user', kind=None)],
                                                                                        values=[
                                                                                            Attribute(
                                                                                                value=Name(id='goal', ctx=Load()),
                                                                                                attr='user_id',
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                        If(
                                                                            test=BoolOp(
                                                                                op=And(),
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Name(id='goal', ctx=Load()),
                                                                                        attr='start_date',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Name(id='field_date_name', ctx=Load()),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='domain', ctx=Load()),
                                                                                            attr='append',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Tuple(
                                                                                                elts=[
                                                                                                    Name(id='field_date_name', ctx=Load()),
                                                                                                    Constant(value='>=', kind=None),
                                                                                                    Attribute(
                                                                                                        value=Name(id='goal', ctx=Load()),
                                                                                                        attr='start_date',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            orelse=[],
                                                                        ),
                                                                        If(
                                                                            test=BoolOp(
                                                                                op=And(),
                                                                                values=[
                                                                                    Attribute(
                                                                                        value=Name(id='goal', ctx=Load()),
                                                                                        attr='end_date',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Name(id='field_date_name', ctx=Load()),
                                                                                ],
                                                                            ),
                                                                            body=[
                                                                                Expr(
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='domain', ctx=Load()),
                                                                                            attr='append',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Tuple(
                                                                                                elts=[
                                                                                                    Name(id='field_date_name', ctx=Load()),
                                                                                                    Constant(value='<=', kind=None),
                                                                                                    Attribute(
                                                                                                        value=Name(id='goal', ctx=Load()),
                                                                                                        attr='end_date',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ),
                                                                            ],
                                                                            orelse=[],
                                                                        ),
                                                                        If(
                                                                            test=Compare(
                                                                                left=Attribute(
                                                                                    value=Name(id='definition', ctx=Load()),
                                                                                    attr='computation_mode',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                ops=[Eq()],
                                                                                comparators=[Constant(value='sum', kind=None)],
                                                                            ),
                                                                            body=[
                                                                                Assign(
                                                                                    targets=[Name(id='field_name', ctx=Store())],
                                                                                    value=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='definition', ctx=Load()),
                                                                                            attr='field_id',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='name',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                                Assign(
                                                                                    targets=[Name(id='res', ctx=Store())],
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='Obj', ctx=Load()),
                                                                                            attr='read_group',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[
                                                                                            Name(id='domain', ctx=Load()),
                                                                                            List(
                                                                                                elts=[Name(id='field_name', ctx=Load())],
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                            List(elts=[], ctx=Load()),
                                                                                        ],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                                Assign(
                                                                                    targets=[Name(id='new_value', ctx=Store())],
                                                                                    value=BoolOp(
                                                                                        op=Or(),
                                                                                        values=[
                                                                                            BoolOp(
                                                                                                op=And(),
                                                                                                values=[
                                                                                                    Name(id='res', ctx=Load()),
                                                                                                    Subscript(
                                                                                                        value=Subscript(
                                                                                                            value=Name(id='res', ctx=Load()),
                                                                                                            slice=Constant(value=0, kind=None),
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        slice=Name(id='field_name', ctx=Load()),
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                            Constant(value=0.0, kind=None),
                                                                                        ],
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                            orelse=[
                                                                                Assign(
                                                                                    targets=[Name(id='new_value', ctx=Store())],
                                                                                    value=Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='Obj', ctx=Load()),
                                                                                            attr='search_count',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Name(id='domain', ctx=Load())],
                                                                                        keywords=[],
                                                                                    ),
                                                                                    type_comment=None,
                                                                                ),
                                                                            ],
                                                                        ),
                                                                        Expr(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='goals_to_write', ctx=Load()),
                                                                                    attr='update',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    Call(
                                                                                        func=Attribute(
                                                                                            value=Name(id='goal', ctx=Load()),
                                                                                            attr='_get_write_values',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        args=[Name(id='new_value', ctx=Load())],
                                                                                        keywords=[],
                                                                                    ),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='_logger', ctx=Load()),
                                                                    attr='error',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Constant(value="Invalid computation mode '%s' in definition %s", kind=None),
                                                                    Attribute(
                                                                        value=Name(id='definition', ctx=Load()),
                                                                        attr='computation_mode',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Attribute(
                                                                        value=Name(id='definition', ctx=Load()),
                                                                        attr='name',
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                For(
                                    target=Tuple(
                                        elts=[
                                            Name(id='goal', ctx=Store()),
                                            Name(id='values', ctx=Store()),
                                        ],
                                        ctx=Store(),
                                    ),
                                    iter=Call(
                                        func=Attribute(
                                            value=Name(id='goals_to_write', ctx=Load()),
                                            attr='items',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    body=[
                                        If(
                                            test=UnaryOp(
                                                op=Not(),
                                                operand=Name(id='values', ctx=Load()),
                                            ),
                                            body=[Continue()],
                                            orelse=[],
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='goal', ctx=Load()),
                                                    attr='write',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='values', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='context',
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='commit_gamification', kind=None)],
                                        keywords=[],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='commit',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_start',
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
                            value=Constant(value='Mark a goal as started.\n\n        This should only be used when creating goals manually (in draft state)', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='state', kind=None)],
                                        values=[Constant(value='inprogress', kind=None)],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='update_goal',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_reach',
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
                            value=Constant(value='Mark a goal as reached.\n\n        If the target goal condition is not met, the state will be reset to In\n        Progress at the next goal update until the end date.', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='state', kind=None)],
                                        values=[Constant(value='reached', kind=None)],
                                    ),
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
                    name='action_fail',
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
                            value=Constant(value='Set the state of the goal to failed.\n\n        A failed goal will be ignored in future checks.', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='state', kind=None)],
                                        values=[Constant(value='failed', kind=None)],
                                    ),
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
                    name='action_cancel',
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
                            value=Constant(value='Reset the completion after setting a goal as reached or failed.\n\n        This is only the current state, if the date and/or target criteria\n        match the conditions for a change of state, this will be applied at the\n        next goal update.', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='state', kind=None)],
                                        values=[Constant(value='inprogress', kind=None)],
                                    ),
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
                    name='create',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals_list', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Goal', ctx=Load()),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='with_context',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[
                                                    keyword(
                                                        arg='no_remind_goal',
                                                        value=Constant(value=True, kind=None),
                                                    ),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals_list', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model_create_multi',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='write',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Overwrite the write method to update the last_update field to today\n\n        If the current value is changed and the report frequency is set to On\n        change, a report is generated\n        ', kind=None),
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='vals', ctx=Load()),
                                    slice=Constant(value='last_update', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='fields', ctx=Load()),
                                        attr='Date',
                                        ctx=Load(),
                                    ),
                                    attr='context_today',
                                    ctx=Load(),
                                ),
                                args=[Name(id='self', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Goal', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[Name(id='vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='goal', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Attribute(
                                                    value=Name(id='goal', ctx=Load()),
                                                    attr='state',
                                                    ctx=Load(),
                                                ),
                                                ops=[NotEq()],
                                                comparators=[Constant(value='draft', kind=None)],
                                            ),
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Compare(
                                                        left=Constant(value='definition_id', kind=None),
                                                        ops=[In()],
                                                        comparators=[Name(id='vals', ctx=Load())],
                                                    ),
                                                    Compare(
                                                        left=Constant(value='user_id', kind=None),
                                                        ops=[In()],
                                                        comparators=[Name(id='vals', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Attribute(
                                                    value=Name(id='exceptions', ctx=Load()),
                                                    attr='UserError',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Can not modify the configuration of a started goal', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='vals', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='current', kind=None)],
                                                keywords=[],
                                            ),
                                            Compare(
                                                left=Constant(value='no_remind_goal', kind=None),
                                                ops=[NotIn()],
                                                comparators=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='context',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        If(
                                            test=Compare(
                                                left=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='goal', ctx=Load()),
                                                        attr='challenge_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='report_message_frequency',
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='onchange', kind=None)],
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='goal', ctx=Load()),
                                                                        attr='challenge_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='sudo',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            attr='report_progress',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='users',
                                                                value=Attribute(
                                                                    value=Name(id='goal', ctx=Load()),
                                                                    attr='user_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                    ),
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_action',
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
                            value=Constant(value='Get the ir.action related to update the goal\n\n        In case of a manual goal, should return a wizard to update the value\n        :return: action description in a dictionary\n        ', kind=None),
                        ),
                        If(
                            test=Attribute(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='definition_id',
                                    ctx=Load(),
                                ),
                                attr='action_id',
                                ctx=Load(),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='action', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='definition_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='action_id',
                                                    ctx=Load(),
                                                ),
                                                attr='read',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='definition_id',
                                            ctx=Load(),
                                        ),
                                        attr='res_id_field',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='current_user', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='user',
                                                        ctx=Load(),
                                                    ),
                                                    attr='with_user',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='user',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='action', ctx=Load()),
                                                    slice=Constant(value='res_id', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Name(id='safe_eval', ctx=Load()),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='definition_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='res_id_field',
                                                        ctx=Load(),
                                                    ),
                                                    Dict(
                                                        keys=[Constant(value='user', kind=None)],
                                                        values=[Name(id='current_user', ctx=Load())],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='action', ctx=Load()),
                                                    slice=Constant(value='views', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    ListComp(
                                                        elt=Tuple(
                                                            elts=[
                                                                Name(id='view_id', ctx=Load()),
                                                                Name(id='mode', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Tuple(
                                                                    elts=[
                                                                        Name(id='view_id', ctx=Store()),
                                                                        Name(id='mode', ctx=Store()),
                                                                    ],
                                                                    ctx=Store(),
                                                                ),
                                                                iter=Subscript(
                                                                    value=Name(id='action', ctx=Load()),
                                                                    slice=Constant(value='views', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                                ifs=[
                                                                    Compare(
                                                                        left=Name(id='mode', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Constant(value='form', kind=None)],
                                                                    ),
                                                                ],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                    Subscript(
                                                        value=Name(id='action', ctx=Load()),
                                                        slice=Constant(value='views', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Return(
                                    value=Name(id='action', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='computation_mode',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='manually', kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='action', ctx=Store())],
                                    value=Dict(
                                        keys=[
                                            Constant(value='name', kind=None),
                                            Constant(value='id', kind=None),
                                            Constant(value='type', kind=None),
                                            Constant(value='views', kind=None),
                                            Constant(value='target', kind=None),
                                            Constant(value='context', kind=None),
                                            Constant(value='res_model', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='Update %s', kind=None),
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='definition_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='name',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='id',
                                                ctx=Load(),
                                            ),
                                            Constant(value='ir.actions.act_window', kind=None),
                                            List(
                                                elts=[
                                                    List(
                                                        elts=[
                                                            Constant(value=False, kind=None),
                                                            Constant(value='form', kind=None),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='new', kind=None),
                                            Dict(
                                                keys=[
                                                    Constant(value='default_goal_id', kind=None),
                                                    Constant(value='default_current', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='current',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Constant(value='gamification.goal.wizard', kind=None),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Name(id='action', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=False, kind=None),
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
