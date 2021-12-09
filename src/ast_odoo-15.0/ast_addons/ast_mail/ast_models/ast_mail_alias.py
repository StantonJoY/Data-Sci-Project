Module(
    body=[
        Import(
            names=[alias(name='ast', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='markupsafe',
            names=[alias(name='Markup', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='_', asname=None),
                alias(name='api', asname=None),
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[
                alias(name='ValidationError', asname=None),
                alias(name='UserError', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='is_html_empty', asname=None),
                alias(name='remove_accents', asname=None),
            ],
            level=0,
        ),
        Assign(
            targets=[Name(id='atext', ctx=Store())],
            value=Constant(value="[a-zA-Z0-9!#$%&'*+\\-/=?^_`{|}~]", kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='dot_atom_text', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='re', ctx=Load()),
                    attr='compile',
                    ctx=Load(),
                ),
                args=[
                    BinOp(
                        left=Constant(value='^%s+(\\.%s+)*$', kind=None),
                        op=Mod(),
                        right=Tuple(
                            elts=[
                                Name(id='atext', ctx=Load()),
                                Name(id='atext', ctx=Load()),
                            ],
                            ctx=Load(),
                        ),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='Alias',
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
                    value=Constant(value="A Mail Alias is a mapping of an email address with a given Odoo Document\n       model. It is used by Odoo's mail gateway when processing incoming emails\n       sent to the system. If the recipient address (To) of the message matches\n       a Mail Alias, the message will be either processed following the rules\n       of that alias. If the message is a reply it will be attached to the\n       existing discussion on the corresponding record, otherwise a new\n       record of the corresponding model will be created.\n\n       This is meant to be used in combination with a catch-all email configuration\n       on the company's mail server, so that as soon as a new mail.alias is\n       created, it becomes immediately usable and Odoo will accept email for it.\n     ", kind=None),
                ),
                Assign(
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='mail.alias', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='Email Aliases', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_rec_name', ctx=Store())],
                    value=Constant(value='alias_name', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_order', ctx=Store())],
                    value=Constant(value='alias_model_id, alias_name', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='alias_name', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Alias Name', kind=None)],
                        keywords=[
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value="The name of the email alias, e.g. 'jobs' if you want to catch emails for <jobs@example.odoo.com>", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='alias_model_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='ir.model', kind=None),
                            Constant(value='Aliased Model', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='ondelete',
                                value=Constant(value='cascade', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The model (Odoo Document Kind) to which this alias corresponds. Any incoming email that does not reply to an existing record will cause the creation of a new record of this model (e.g. a Project Task)', kind=None),
                            ),
                            keyword(
                                arg='domain',
                                value=Constant(value="[('field_id.name', '=', 'message_ids')]", kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='alias_user_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='res.users', kind=None),
                            Constant(value='Owner', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='default',
                                value=Lambda(
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='self', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='user',
                                        ctx=Load(),
                                    ),
                                ),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='The owner of records created upon receiving emails on this alias. If this field is not set the system will attempt to find the right owner based on the sender (From) address, or will use the Administrator account if no system user is found for that address.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='alias_defaults', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Text',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Default Values', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='{}', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='A Python dictionary that will be evaluated to provide default values when creating new records for this alias.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='alias_force_thread_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Record Thread ID', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Optional ID of a thread (record) to which all incoming messages will be attached, even if they did not reply to it. If set, this will disable the creation of new records completely.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='alias_domain', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Alias domain', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_alias_domain', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='alias_parent_model_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Many2one',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='ir.model', kind=None),
                            Constant(value='Parent Model', kind=None),
                        ],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Parent model holding the alias. The model holding the alias reference is not necessarily the model given by alias_model_id (example: project (parent_model) and task (model))', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='alias_parent_thread_id', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Integer',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Parent Record Thread ID', kind=None)],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='ID of the parent record holding the alias (example: project holding the task creation alias)', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='alias_contact', ctx=Store())],
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
                                            Constant(value='everyone', kind=None),
                                            Constant(value='Everyone', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='partners', kind=None),
                                            Constant(value='Authenticated Partners', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='followers', kind=None),
                                            Constant(value='Followers only', kind=None),
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
                                value=Constant(value='everyone', kind=None),
                            ),
                            keyword(
                                arg='string',
                                value=Constant(value='Alias Contact Security', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Policy to post a message on the document using the mailgateway.\n- everyone: everyone can post\n- partners: only authenticated partners\n- followers: only followers of the related document or members of following channels\n', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='alias_bounced_content', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Html',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Custom Bounced Message', kind=None)],
                        keywords=[
                            keyword(
                                arg='translate',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='If set, this content will automatically be sent out to unauthorized users instead of the default message.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_sql_constraints', ctx=Store())],
                    value=List(
                        elts=[
                            Tuple(
                                elts=[
                                    Constant(value='alias_unique', kind=None),
                                    Constant(value='UNIQUE(alias_name)', kind=None),
                                    Constant(value='Unfortunately this email alias is already used, please choose a unique one', kind=None),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_alias_is_ascii',
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
                            value=Constant(value=' The local-part ("display-name" <local-part@domain>) of an\n            address only contains limited range of ascii characters.\n            We DO NOT allow anything else than ASCII dot-atom formed\n            local-part. Quoted-string and internationnal characters are\n            to be rejected. See rfc5322 sections 3.4.1 and 3.2.3\n        ', kind=None),
                        ),
                        For(
                            target=Name(id='alias', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='alias', ctx=Load()),
                                                attr='alias_name',
                                                ctx=Load(),
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Call(
                                                    func=Attribute(
                                                        value=Name(id='dot_atom_text', ctx=Load()),
                                                        attr='match',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Attribute(
                                                            value=Name(id='alias', ctx=Load()),
                                                            attr='alias_name',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[
                                                            Constant(value='You cannot use anything else than unaccented latin characters in the alias address (%s).', kind=None),
                                                            Attribute(
                                                                value=Name(id='alias', ctx=Load()),
                                                                attr='alias_name',
                                                                ctx=Load(),
                                                            ),
                                                        ],
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
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[Constant(value='alias_name', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_alias_domain',
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
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='alias_domain',
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.config_parameter', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='mail.catchall.domain', kind=None)],
                                keywords=[],
                            ),
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
                            args=[Constant(value='alias_name', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_alias_defaults',
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
                            target=Name(id='alias', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Try(
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='ast', ctx=Load()),
                                                            attr='literal_eval',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='alias', ctx=Load()),
                                                                attr='alias_defaults',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=Name(id='Exception', ctx=Load()),
                                            name=None,
                                            body=[
                                                Raise(
                                                    exc=Call(
                                                        func=Name(id='ValidationError', ctx=Load()),
                                                        args=[
                                                            Call(
                                                                func=Name(id='_', ctx=Load()),
                                                                args=[Constant(value='Invalid expression, it must be a literal python dictionary definition e.g. "{\'field\': \'value\'}"', kind=None)],
                                                                keywords=[],
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
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[Constant(value='alias_defaults', kind=None)],
                            keywords=[],
                        ),
                    ],
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
                        Expr(
                            value=Constant(value=' Creates email.alias records according to the values provided in\n        ``vals`` with 1 alteration:\n\n          * ``alias_name`` value may be cleaned by replacing certain unsafe\n            characters;\n\n        :raise UserError: if given alias_name is already assigned or there are\n        duplicates in given vals_list;\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='alias_names', ctx=Store())],
                            value=ListComp(
                                elt=Subscript(
                                    value=Name(id='vals', ctx=Load()),
                                    slice=Constant(value='alias_name', kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='vals', ctx=Store()),
                                        iter=Name(id='vals_list', ctx=Load()),
                                        ifs=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='vals', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='alias_name', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='alias_names', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='sanitized_names', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_clean_and_check_unique',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='alias_names', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='vals', ctx=Store()),
                                    iter=Name(id='vals_list', ctx=Load()),
                                    body=[
                                        If(
                                            test=Call(
                                                func=Attribute(
                                                    value=Name(id='vals', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='alias_name', kind=None)],
                                                keywords=[],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='vals', ctx=Load()),
                                                            slice=Constant(value='alias_name', kind=None),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Subscript(
                                                        value=Name(id='sanitized_names', ctx=Load()),
                                                        slice=Call(
                                                            func=Attribute(
                                                                value=Name(id='alias_names', ctx=Load()),
                                                                attr='index',
                                                                ctx=Load(),
                                                            ),
                                                            args=[
                                                                Subscript(
                                                                    value=Name(id='vals', ctx=Load()),
                                                                    slice=Constant(value='alias_name', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            keywords=[],
                                                        ),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
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
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Alias', ctx=Load()),
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
                            value=Constant(value='"Raises UserError if given alias name is already assigned', kind=None),
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
                                        args=[Constant(value='alias_name', kind=None)],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[Name(id='self', ctx=Load())],
                                            keywords=[],
                                        ),
                                        ops=[Gt()],
                                        comparators=[Constant(value=1, kind=None)],
                                    ),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='Email alias %(alias_name)s cannot be used on %(count)d records at the same time. Please update records one by one.', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                arg='alias_name',
                                                                value=Subscript(
                                                                    value=Name(id='vals', ctx=Load()),
                                                                    slice=Constant(value='alias_name', kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='count',
                                                                value=Call(
                                                                    func=Name(id='len', ctx=Load()),
                                                                    args=[Name(id='self', ctx=Load())],
                                                                    keywords=[],
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
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='vals', ctx=Load()),
                                            slice=Constant(value='alias_name', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_clean_and_check_unique',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                List(
                                                    elts=[
                                                        Call(
                                                            func=Attribute(
                                                                value=Name(id='vals', ctx=Load()),
                                                                attr='get',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Constant(value='alias_name', kind=None)],
                                                            keywords=[],
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='Alias', ctx=Load()),
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
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='name_get',
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
                            value=Constant(value='Return the mail alias display alias_name, including the implicit\n           mail catchall domain if exists from config otherwise "New Alias".\n           e.g. `jobs@mail.odoo.com` or `jobs` or \'New Alias\'\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='alias_name',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='alias_domain',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='res', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Tuple(
                                                        elts=[
                                                            Subscript(
                                                                value=Name(id='record', ctx=Load()),
                                                                slice=Constant(value='id', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            BinOp(
                                                                left=Constant(value='%s@%s', kind=None),
                                                                op=Mod(),
                                                                right=Tuple(
                                                                    elts=[
                                                                        Attribute(
                                                                            value=Name(id='record', ctx=Load()),
                                                                            attr='alias_name',
                                                                            ctx=Load(),
                                                                        ),
                                                                        Attribute(
                                                                            value=Name(id='record', ctx=Load()),
                                                                            attr='alias_domain',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Attribute(
                                                value=Name(id='record', ctx=Load()),
                                                attr='alias_name',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='res', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Tuple(
                                                                elts=[
                                                                    Subscript(
                                                                        value=Name(id='record', ctx=Load()),
                                                                        slice=Constant(value='id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    BinOp(
                                                                        left=Constant(value='%s', kind=None),
                                                                        op=Mod(),
                                                                        right=Attribute(
                                                                            value=Name(id='record', ctx=Load()),
                                                                            attr='alias_name',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
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
                                                            value=Name(id='res', ctx=Load()),
                                                            attr='append',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Tuple(
                                                                elts=[
                                                                    Subscript(
                                                                        value=Name(id='record', ctx=Load()),
                                                                        slice=Constant(value='id', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='Inactive Alias', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ],
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
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='res', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_clean_and_check_unique',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='names', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='When an alias name appears to already be an email, we keep the local\n        part only. A sanitizing / cleaning is also performed on the name. If\n        name already exists an UserError is raised. ', kind=None),
                        ),
                        FunctionDef(
                            name='_sanitize_alias_name',
                            args=arguments(
                                posonlyargs=[],
                                args=[arg(arg='name', annotation=None, type_comment=None)],
                                vararg=None,
                                kwonlyargs=[],
                                kw_defaults=[],
                                kwarg=None,
                                defaults=[],
                            ),
                            body=[
                                Expr(
                                    value=Constant(value=' Cleans and sanitizes the alias name ', kind=None),
                                ),
                                Assign(
                                    targets=[Name(id='sanitized_name', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Call(
                                                            func=Name(id='remove_accents', ctx=Load()),
                                                            args=[Name(id='name', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                        attr='lower',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='@', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='sanitized_name', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='sub',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='[^\\w+.]+', kind=None),
                                            Constant(value='-', kind=None),
                                            Name(id='sanitized_name', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='sanitized_name', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='re', ctx=Load()),
                                            attr='sub',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='^\\.+|\\.+$|\\.+(?=\\.)', kind=None),
                                            Constant(value='', kind=None),
                                            Name(id='sanitized_name', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='sanitized_name', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='sanitized_name', ctx=Load()),
                                                    attr='encode',
                                                    ctx=Load(),
                                                ),
                                                args=[Constant(value='ascii', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='errors',
                                                        value=Constant(value='replace', kind=None),
                                                    ),
                                                ],
                                            ),
                                            attr='decode',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Return(
                                    value=Name(id='sanitized_name', ctx=Load()),
                                ),
                            ],
                            decorator_list=[],
                            returns=None,
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sanitized_names', ctx=Store())],
                            value=ListComp(
                                elt=Call(
                                    func=Name(id='_sanitize_alias_name', ctx=Load()),
                                    args=[Name(id='name', ctx=Load())],
                                    keywords=[],
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='name', ctx=Store()),
                                        iter=Name(id='names', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='catchall_alias', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.config_parameter', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='mail.catchall.alias', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='bounce_alias', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.config_parameter', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='mail.bounce.alias', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='alias_domain', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.config_parameter', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='get_param',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='mail.catchall.domain', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='sanitized_name', ctx=Store()),
                            iter=Name(id='sanitized_names', ctx=Load()),
                            body=[
                                If(
                                    test=Compare(
                                        left=Name(id='sanitized_name', ctx=Load()),
                                        ops=[In()],
                                        comparators=[
                                            List(
                                                elts=[
                                                    Name(id='catchall_alias', ctx=Load()),
                                                    Name(id='bounce_alias', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='matching_alias_name', ctx=Store())],
                                            value=IfExp(
                                                test=Name(id='alias_domain', ctx=Load()),
                                                body=BinOp(
                                                    left=Constant(value='%s@%s', kind=None),
                                                    op=Mod(),
                                                    right=Tuple(
                                                        elts=[
                                                            Name(id='sanitized_name', ctx=Load()),
                                                            Name(id='alias_domain', ctx=Load()),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ),
                                                orelse=Name(id='sanitized_name', ctx=Load()),
                                            ),
                                            type_comment=None,
                                        ),
                                        Raise(
                                            exc=Call(
                                                func=Name(id='UserError', ctx=Load()),
                                                args=[
                                                    Call(
                                                        func=Name(id='_', ctx=Load()),
                                                        args=[Constant(value='The e-mail alias %(matching_alias_name)s is already used as %(alias_duplicate)s alias. Please choose another alias.', kind=None)],
                                                        keywords=[
                                                            keyword(
                                                                arg='matching_alias_name',
                                                                value=Name(id='matching_alias_name', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='alias_duplicate',
                                                                value=IfExp(
                                                                    test=Compare(
                                                                        left=Name(id='sanitized_name', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Name(id='catchall_alias', ctx=Load())],
                                                                    ),
                                                                    body=Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='catchall', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                    orelse=Call(
                                                                        func=Name(id='_', ctx=Load()),
                                                                        args=[Constant(value='bounce', kind=None)],
                                                                        keywords=[],
                                                                    ),
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
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='domain', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='alias_name', kind=None),
                                            Constant(value='in', kind=None),
                                            Name(id='sanitized_names', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='self', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='domain', ctx=Store()),
                                    op=Add(),
                                    value=List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='id', kind=None),
                                                    Constant(value='not in', kind=None),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='ids',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='matching_alias', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[Name(id='domain', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=1, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='matching_alias', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Name(id='sanitized_names', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='sanitized_alias_name', ctx=Store())],
                            value=Call(
                                func=Name(id='_sanitize_alias_name', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='matching_alias', ctx=Load()),
                                        attr='alias_name',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='matching_alias_name', ctx=Store())],
                            value=IfExp(
                                test=Name(id='alias_domain', ctx=Load()),
                                body=BinOp(
                                    left=Constant(value='%s@%s', kind=None),
                                    op=Mod(),
                                    right=Tuple(
                                        elts=[
                                            Name(id='sanitized_alias_name', ctx=Load()),
                                            Name(id='alias_domain', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                ),
                                orelse=Name(id='sanitized_alias_name', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Attribute(
                                        value=Name(id='matching_alias', ctx=Load()),
                                        attr='alias_parent_model_id',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='matching_alias', ctx=Load()),
                                        attr='alias_parent_thread_id',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='document_name', ctx=Store())],
                                    value=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='matching_alias', ctx=Load()),
                                                                    attr='alias_parent_model_id',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='model',
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        attr='sudo',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                attr='browse',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Attribute(
                                                    value=Name(id='matching_alias', ctx=Load()),
                                                    attr='alias_parent_thread_id',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='display_name',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Raise(
                                    exc=Call(
                                        func=Name(id='UserError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='The e-mail alias %(matching_alias_name)s is already used by the %(document_name)s %(model_name)s. Choose another alias or change it on the other document.', kind=None)],
                                                keywords=[
                                                    keyword(
                                                        arg='matching_alias_name',
                                                        value=Name(id='matching_alias_name', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='document_name',
                                                        value=Name(id='document_name', ctx=Load()),
                                                    ),
                                                    keyword(
                                                        arg='model_name',
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Name(id='matching_alias', ctx=Load()),
                                                                attr='alias_parent_model_id',
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
                        Raise(
                            exc=Call(
                                func=Name(id='UserError', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='The e-mail alias %(matching_alias_name)s is already linked with %(alias_model_name)s. Choose another alias or change it on the linked model.', kind=None)],
                                        keywords=[
                                            keyword(
                                                arg='matching_alias_name',
                                                value=Name(id='matching_alias_name', ctx=Load()),
                                            ),
                                            keyword(
                                                arg='alias_model_name',
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='matching_alias', ctx=Load()),
                                                        attr='alias_model_id',
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
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='open_document',
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
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='alias_model_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='alias_force_thread_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='res_id', kind=None),
                                    Constant(value='type', kind=None),
                                ],
                                values=[
                                    Constant(value='form', kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='alias_model_id',
                                            ctx=Load(),
                                        ),
                                        attr='model',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='alias_force_thread_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='ir.actions.act_window', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='open_parent_document',
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
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='alias_parent_model_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='alias_parent_thread_id',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=False, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='view_mode', kind=None),
                                    Constant(value='res_model', kind=None),
                                    Constant(value='res_id', kind=None),
                                    Constant(value='type', kind=None),
                                ],
                                values=[
                                    Constant(value='form', kind=None),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='alias_parent_model_id',
                                            ctx=Load(),
                                        ),
                                        attr='model',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='alias_parent_thread_id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='ir.actions.act_window', kind=None),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_alias_bounced_body_fallback',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='message_dict', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='contact_description', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_alias_contact_description',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='default_email', ctx=Store())],
                            value=IfExp(
                                test=Attribute(
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
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    attr='email',
                                    ctx=Load(),
                                ),
                                body=Attribute(
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
                                        attr='partner_id',
                                        ctx=Load(),
                                    ),
                                    attr='email_formatted',
                                    ctx=Load(),
                                ),
                                orelse=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='company',
                                        ctx=Load(),
                                    ),
                                    attr='name',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=BinOp(
                                left=Call(
                                    func=Name(id='Markup', ctx=Load()),
                                    args=[
                                        Call(
                                            func=Name(id='_', ctx=Load()),
                                            args=[Constant(value='<p>Dear Sender,<br /><br />\nThe message below could not be accepted by the address %(alias_display_name)s.\nOnly %(contact_description)s are allowed to contact it.<br /><br />\nPlease make sure you are using the correct address or contact us at %(default_email)s instead.<br /><br />\nKind Regards,</p>', kind=None)],
                                            keywords=[],
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                op=Mod(),
                                right=Dict(
                                    keys=[
                                        Constant(value='alias_display_name', kind=None),
                                        Constant(value='contact_description', kind=None),
                                        Constant(value='default_email', kind=None),
                                    ],
                                    values=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='display_name',
                                            ctx=Load(),
                                        ),
                                        Name(id='contact_description', ctx=Load()),
                                        Name(id='default_email', ctx=Load()),
                                    ],
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_alias_contact_description',
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
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='alias_contact',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='partners', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='addresses linked to registered partners', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Name(id='_', ctx=Load()),
                                args=[Constant(value='some specific addresses', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_alias_bounced_body',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='message_dict', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Get the body of the email return in case of bounced email.\n\n        :param message_dict: dictionary of mail values\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='lang_author', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Name(id='message_dict', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='author_id', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Try(
                                    body=[
                                        Assign(
                                            targets=[Name(id='lang_author', ctx=Store())],
                                            value=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='res.partner', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='browse',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        Subscript(
                                                            value=Name(id='message_dict', ctx=Load()),
                                                            slice=Constant(value='author_id', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                                attr='lang',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    handlers=[
                                        ExceptHandler(
                                            type=None,
                                            name=None,
                                            body=[Pass()],
                                        ),
                                    ],
                                    orelse=[],
                                    finalbody=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='lang_author', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='self', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=Name(id='lang_author', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Call(
                                    func=Name(id='is_html_empty', ctx=Load()),
                                    args=[
                                        Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='alias_bounced_content',
                                            ctx=Load(),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='body', ctx=Store())],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='alias_bounced_content',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='body', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_alias_bounced_body_fallback',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='message_dict', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='template', ctx=Store())],
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
                                args=[Constant(value='mail.mail_bounce_alias_security', kind=None)],
                                keywords=[
                                    keyword(
                                        arg='raise_if_not_found',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='template', ctx=Load()),
                                    attr='_render',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='body', kind=None),
                                            Constant(value='message', kind=None),
                                        ],
                                        values=[
                                            Name(id='body', ctx=Load()),
                                            Name(id='message_dict', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='engine',
                                        value=Constant(value='ir.qweb', kind=None),
                                    ),
                                    keyword(
                                        arg='minimal_qcontext',
                                        value=Constant(value=True, kind=None),
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
