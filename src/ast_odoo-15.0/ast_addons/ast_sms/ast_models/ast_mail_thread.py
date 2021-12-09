Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='fields', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.phone_validation.tools',
            names=[alias(name='phone_validation', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='html2plaintext', asname=None),
                alias(name='plaintext2html', asname=None),
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
        ClassDef(
            name='MailThread',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='mail.thread', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='message_has_sms_error', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[Constant(value='SMS Delivery error', kind=None)],
                        keywords=[
                            keyword(
                                arg='compute',
                                value=Constant(value='_compute_message_has_sms_error', kind=None),
                            ),
                            keyword(
                                arg='search',
                                value=Constant(value='_search_message_has_sms_error', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='If checked, some messages have a delivery error.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_compute_message_has_sms_error',
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
                            targets=[Name(id='res', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                        If(
                            test=Attribute(
                                value=Name(id='self', ctx=Load()),
                                attr='ids',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_cr',
                                                ctx=Load(),
                                            ),
                                            attr='execute',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value=" SELECT msg.res_id, COUNT(msg.res_id) FROM mail_message msg\n                                 RIGHT JOIN mail_notification rel\n                                 ON rel.mail_message_id = msg.id AND rel.notification_type = 'sms' AND rel.notification_status in ('exception')\n                                 WHERE msg.author_id = %s AND msg.model = %s AND msg.res_id in %s AND msg.message_type != 'user_notification'\n                                 GROUP BY msg.res_id", kind=None),
                                            Tuple(
                                                elts=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='user',
                                                                ctx=Load(),
                                                            ),
                                                            attr='partner_id',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_name',
                                                        ctx=Load(),
                                                    ),
                                                    Call(
                                                        func=Name(id='tuple', ctx=Load()),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='ids',
                                                                ctx=Load(),
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
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='res', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='_cr',
                                                        ctx=Load(),
                                                    ),
                                                    attr='fetchall',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='message_has_sms_error',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='bool', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='res', ctx=Load()),
                                                    attr='get',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Attribute(
                                                            value=Name(id='record', ctx=Load()),
                                                            attr='_origin',
                                                            ctx=Load(),
                                                        ),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=0, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
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
                    name='_search_message_has_sms_error',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='operator', annotation=None, type_comment=None),
                            arg(arg='operand', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Return(
                            value=List(
                                elts=[
                                    Constant(value='&', kind=None),
                                    Tuple(
                                        elts=[
                                            Constant(value='message_ids.has_sms_error', kind=None),
                                            Name(id='operator', ctx=Load()),
                                            Name(id='operand', ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='message_ids.author_id', kind=None),
                                            Constant(value='=', kind=None),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='user',
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
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_sms_get_partner_fields',
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
                            value=Constant(value=' This method returns the fields to use to find the contact to link\n        whensending an SMS. Having partner is not necessary, having only phone\n        number fields is possible. However it gives more flexibility to\n        notifications management when having partners. ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='fields', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        If(
                            test=Call(
                                func=Name(id='hasattr', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Constant(value='partner_id', kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='fields', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='partner_id', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Call(
                                func=Name(id='hasattr', ctx=Load()),
                                args=[
                                    Name(id='self', ctx=Load()),
                                    Constant(value='partner_ids', kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='fields', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='partner_ids', kind=None)],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='fields', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_sms_get_default_partners',
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
                            value=Constant(value=' This method will likely need to be overridden by inherited models.\n               :returns partners: recordset of res.partner\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='partners', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='res.partner', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='fname', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_sms_get_partner_fields',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='partners', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='partners', ctx=Load()),
                                            attr='union',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Starred(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='mapped',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='fname', ctx=Load())],
                                                    keywords=[],
                                                ),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='partners', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_sms_get_number_fields',
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
                            value=Constant(value=' This method returns the fields to use to find the number to use to\n        send an SMS on a record. ', kind=None),
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='mobile', kind=None),
                                ops=[In()],
                                comparators=[Name(id='self', ctx=Load())],
                            ),
                            body=[
                                Return(
                                    value=List(
                                        elts=[Constant(value='mobile', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=List(elts=[], ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_sms_get_recipients_info',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='force_field', annotation=None, type_comment=None),
                            arg(arg='partner_fallback', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=True, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='" Get SMS recipient information on current record set. This method\n        checks for numbers and sanitation in order to centralize computation.\n\n        Example of use cases\n\n          * click on a field -> number is actually forced from field, find customer\n            linked to record, force its number to field or fallback on customer fields;\n          * contact -> find numbers from all possible phone fields on record, find\n            customer, force its number to found field number or fallback on customer fields;\n\n        :param force_field: either give a specific field to find phone number, either\n            generic heuristic is used to find one based on ``_sms_get_number_fields``;\n        :param partner_fallback: if no value found in the record, check its customer\n            values based on ``_sms_get_default_partners``;\n\n        :return dict: record.id: {\n            \'partner\': a res.partner recordset that is the customer (void or singleton)\n                linked to the recipient. See ``_sms_get_default_partners``;\n            \'sanitized\': sanitized number to use (coming from record\'s field or partner\'s\n                phone fields). Set to False is number impossible to parse and format;\n            \'number\': original number before sanitation;\n            \'partner_store\': whether the number comes from the customer phone fields. If\n                False it means number comes from the record itself, even if linked to a\n                customer;\n            \'field_store\': field in which the number has been found (generally mobile or\n                phone, see ``_sms_get_number_fields``);\n        } for each record in self\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='dict', ctx=Load()),
                                    attr='fromkeys',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='tocheck_fields', ctx=Store())],
                            value=IfExp(
                                test=Name(id='force_field', ctx=Load()),
                                body=List(
                                    elts=[Name(id='force_field', ctx=Load())],
                                    ctx=Load(),
                                ),
                                orelse=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_sms_get_number_fields',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='record', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='all_numbers', ctx=Store())],
                                    value=ListComp(
                                        elt=Subscript(
                                            value=Name(id='record', ctx=Load()),
                                            slice=Name(id='fname', ctx=Load()),
                                            ctx=Load(),
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='fname', ctx=Store()),
                                                iter=Name(id='tocheck_fields', ctx=Load()),
                                                ifs=[
                                                    Compare(
                                                        left=Name(id='fname', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[Name(id='record', ctx=Load())],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='all_partners', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='record', ctx=Load()),
                                            attr='_sms_get_default_partners',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='valid_number', ctx=Store())],
                                    value=Constant(value=False, kind=None),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='fname', ctx=Store()),
                                    iter=ListComp(
                                        elt=Name(id='f', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='f', ctx=Store()),
                                                iter=Name(id='tocheck_fields', ctx=Load()),
                                                ifs=[
                                                    Compare(
                                                        left=Name(id='f', ctx=Load()),
                                                        ops=[In()],
                                                        comparators=[Name(id='record', ctx=Load())],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='valid_number', ctx=Store())],
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='phone_validation', ctx=Load()),
                                                            attr='phone_sanitize_numbers_w_record',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            List(
                                                                elts=[
                                                                    Subscript(
                                                                        value=Name(id='record', ctx=Load()),
                                                                        slice=Name(id='fname', ctx=Load()),
                                                                        ctx=Load(),
                                                                    ),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Name(id='record', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    slice=Subscript(
                                                        value=Name(id='record', ctx=Load()),
                                                        slice=Name(id='fname', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='sanitized', kind=None),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='valid_number', ctx=Load()),
                                            body=[Break()],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='valid_number', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='result', ctx=Load()),
                                                    slice=Attribute(
                                                        value=Name(id='record', ctx=Load()),
                                                        attr='id',
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Dict(
                                                keys=[
                                                    Constant(value='partner', kind=None),
                                                    Constant(value='sanitized', kind=None),
                                                    Constant(value='number', kind=None),
                                                    Constant(value='partner_store', kind=None),
                                                    Constant(value='field_store', kind=None),
                                                ],
                                                values=[
                                                    IfExp(
                                                        test=Name(id='all_partners', ctx=Load()),
                                                        body=Subscript(
                                                            value=Name(id='all_partners', ctx=Load()),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        orelse=Subscript(
                                                            value=Attribute(
                                                                value=Name(id='self', ctx=Load()),
                                                                attr='env',
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='res.partner', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    Name(id='valid_number', ctx=Load()),
                                                    Subscript(
                                                        value=Name(id='record', ctx=Load()),
                                                        slice=Name(id='fname', ctx=Load()),
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=False, kind=None),
                                                    Name(id='fname', ctx=Load()),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=BoolOp(
                                                op=And(),
                                                values=[
                                                    Name(id='all_partners', ctx=Load()),
                                                    Name(id='partner_fallback', ctx=Load()),
                                                ],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='partner', ctx=Store())],
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='res.partner', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                                For(
                                                    target=Name(id='partner', ctx=Store()),
                                                    iter=Name(id='all_partners', ctx=Load()),
                                                    body=[
                                                        For(
                                                            target=Name(id='fname', ctx=Store()),
                                                            iter=Call(
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
                                                                    attr='_sms_get_number_fields',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='valid_number', ctx=Store())],
                                                                    value=Subscript(
                                                                        value=Subscript(
                                                                            value=Call(
                                                                                func=Attribute(
                                                                                    value=Name(id='phone_validation', ctx=Load()),
                                                                                    attr='phone_sanitize_numbers_w_record',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[
                                                                                    List(
                                                                                        elts=[
                                                                                            Subscript(
                                                                                                value=Name(id='partner', ctx=Load()),
                                                                                                slice=Name(id='fname', ctx=Load()),
                                                                                                ctx=Load(),
                                                                                            ),
                                                                                        ],
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    Name(id='record', ctx=Load()),
                                                                                ],
                                                                                keywords=[],
                                                                            ),
                                                                            slice=Subscript(
                                                                                value=Name(id='partner', ctx=Load()),
                                                                                slice=Name(id='fname', ctx=Load()),
                                                                                ctx=Load(),
                                                                            ),
                                                                            ctx=Load(),
                                                                        ),
                                                                        slice=Constant(value='sanitized', kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Name(id='valid_number', ctx=Load()),
                                                                    body=[Break()],
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
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='valid_number', ctx=Load()),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='fname', ctx=Store())],
                                                            value=IfExp(
                                                                test=Attribute(
                                                                    value=Name(id='partner', ctx=Load()),
                                                                    attr='mobile',
                                                                    ctx=Load(),
                                                                ),
                                                                body=Constant(value='mobile', kind=None),
                                                                orelse=IfExp(
                                                                    test=Attribute(
                                                                        value=Name(id='partner', ctx=Load()),
                                                                        attr='phone',
                                                                        ctx=Load(),
                                                                    ),
                                                                    body=Constant(value='phone', kind=None),
                                                                    orelse=Constant(value='mobile', kind=None),
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                                Assign(
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='result', ctx=Load()),
                                                            slice=Attribute(
                                                                value=Name(id='record', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Dict(
                                                        keys=[
                                                            Constant(value='partner', kind=None),
                                                            Constant(value='sanitized', kind=None),
                                                            Constant(value='number', kind=None),
                                                            Constant(value='partner_store', kind=None),
                                                            Constant(value='field_store', kind=None),
                                                        ],
                                                        values=[
                                                            Name(id='partner', ctx=Load()),
                                                            IfExp(
                                                                test=Name(id='valid_number', ctx=Load()),
                                                                body=Name(id='valid_number', ctx=Load()),
                                                                orelse=Constant(value=False, kind=None),
                                                            ),
                                                            Subscript(
                                                                value=Name(id='partner', ctx=Load()),
                                                                slice=Name(id='fname', ctx=Load()),
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=True, kind=None),
                                                            Name(id='fname', ctx=Load()),
                                                        ],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                Assign(
                                                    targets=[
                                                        Tuple(
                                                            elts=[
                                                                Name(id='value', ctx=Store()),
                                                                Name(id='fname', ctx=Store()),
                                                            ],
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Call(
                                                        func=Name(id='next', ctx=Load()),
                                                        args=[
                                                            GeneratorExp(
                                                                elt=Tuple(
                                                                    elts=[
                                                                        Name(id='value', ctx=Load()),
                                                                        Name(id='fname', ctx=Load()),
                                                                    ],
                                                                    ctx=Load(),
                                                                ),
                                                                generators=[
                                                                    comprehension(
                                                                        target=Tuple(
                                                                            elts=[
                                                                                Name(id='value', ctx=Store()),
                                                                                Name(id='fname', ctx=Store()),
                                                                            ],
                                                                            ctx=Store(),
                                                                        ),
                                                                        iter=Call(
                                                                            func=Name(id='zip', ctx=Load()),
                                                                            args=[
                                                                                Name(id='all_numbers', ctx=Load()),
                                                                                Name(id='tocheck_fields', ctx=Load()),
                                                                            ],
                                                                            keywords=[],
                                                                        ),
                                                                        ifs=[Name(id='value', ctx=Load())],
                                                                        is_async=0,
                                                                    ),
                                                                ],
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value=False, kind=None),
                                                                    IfExp(
                                                                        test=Name(id='tocheck_fields', ctx=Load()),
                                                                        body=Subscript(
                                                                            value=Name(id='tocheck_fields', ctx=Load()),
                                                                            slice=Constant(value=0, kind=None),
                                                                            ctx=Load(),
                                                                        ),
                                                                        orelse=Constant(value=False, kind=None),
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
                                                    targets=[
                                                        Subscript(
                                                            value=Name(id='result', ctx=Load()),
                                                            slice=Attribute(
                                                                value=Name(id='record', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            ctx=Store(),
                                                        ),
                                                    ],
                                                    value=Dict(
                                                        keys=[
                                                            Constant(value='partner', kind=None),
                                                            Constant(value='sanitized', kind=None),
                                                            Constant(value='number', kind=None),
                                                            Constant(value='partner_store', kind=None),
                                                            Constant(value='field_store', kind=None),
                                                        ],
                                                        values=[
                                                            Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='self', ctx=Load()),
                                                                    attr='env',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='res.partner', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value=False, kind=None),
                                                            Name(id='value', ctx=Load()),
                                                            Constant(value=False, kind=None),
                                                            Name(id='fname', ctx=Load()),
                                                        ],
                                                    ),
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
                        Return(
                            value=Name(id='result', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_message_sms_schedule_mass',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='body', annotation=None, type_comment=None),
                            arg(arg='template', annotation=None, type_comment=None),
                            arg(arg='active_domain', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='composer_values', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value='', kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Shortcut method to schedule a mass sms sending on a recordset.\n\n        :param template: an optional sms.template record;\n        :param active_domain: bypass self.ids and apply composer on active_domain\n          instead;\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='composer_context', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='default_res_model', kind=None),
                                    Constant(value='default_composition_mode', kind=None),
                                    Constant(value='default_template_id', kind=None),
                                    Constant(value='default_body', kind=None),
                                ],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_name',
                                        ctx=Load(),
                                    ),
                                    Constant(value='mass', kind=None),
                                    IfExp(
                                        test=Name(id='template', ctx=Load()),
                                        body=Attribute(
                                            value=Name(id='template', ctx=Load()),
                                            attr='id',
                                            ctx=Load(),
                                        ),
                                        orelse=Constant(value=False, kind=None),
                                    ),
                                    IfExp(
                                        test=BoolOp(
                                            op=And(),
                                            values=[
                                                Name(id='body', ctx=Load()),
                                                UnaryOp(
                                                    op=Not(),
                                                    operand=Name(id='template', ctx=Load()),
                                                ),
                                            ],
                                        ),
                                        body=Name(id='body', ctx=Load()),
                                        orelse=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='active_domain', ctx=Load()),
                                ops=[IsNot()],
                                comparators=[Constant(value=None, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='composer_context', ctx=Load()),
                                            slice=Constant(value='default_use_active_domain', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Constant(value=True, kind=None),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='composer_context', ctx=Load()),
                                            slice=Constant(value='default_active_domain', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Name(id='repr', ctx=Load()),
                                        args=[Name(id='active_domain', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='composer_context', ctx=Load()),
                                            slice=Constant(value='default_res_ids', kind=None),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='ids',
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                        ),
                        Assign(
                            targets=[Name(id='create_vals', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='mass_force_send', kind=None),
                                    Constant(value='mass_keep_log', kind=None),
                                ],
                                values=[
                                    Constant(value=False, kind=None),
                                    Constant(value=True, kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='composer_values', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='create_vals', ctx=Load()),
                                            attr='update',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='composer_values', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='composer', ctx=Store())],
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
                                                slice=Constant(value='sms.composer', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg=None,
                                                value=Name(id='composer_context', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    attr='create',
                                    ctx=Load(),
                                ),
                                args=[Name(id='create_vals', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='composer', ctx=Load()),
                                    attr='_action_send_sms',
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
                    name='_message_sms_with_template',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='template', annotation=None, type_comment=None),
                            arg(arg='template_xmlid', annotation=None, type_comment=None),
                            arg(arg='template_fallback', annotation=None, type_comment=None),
                            arg(arg='partner_ids', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value='', kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Shortcut method to perform a _message_sms with an sms.template.\n\n        :param template: a valid sms.template record;\n        :param template_xmlid: XML ID of an sms.template (if no template given);\n        :param template_fallback: plaintext (inline_template-enabled) in case template\n          and template xml id are falsy (for example due to deleted data);\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='template', ctx=Load()),
                                    ),
                                    Name(id='template_xmlid', ctx=Load()),
                                ],
                            ),
                            body=[
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
                                        args=[Name(id='template_xmlid', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='raise_if_not_found',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='template', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='body', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='template', ctx=Load()),
                                                attr='_render_field',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Constant(value='body', kind=None),
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
                            ],
                            orelse=[
                                Assign(
                                    targets=[Name(id='body', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Subscript(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    slice=Constant(value='sms.template', kind=None),
                                                    ctx=Load(),
                                                ),
                                                attr='_render_template',
                                                ctx=Load(),
                                            ),
                                            args=[
                                                Name(id='template_fallback', ctx=Load()),
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='_name',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='ids',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
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
                            ],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_message_sms',
                                    ctx=Load(),
                                ),
                                args=[Name(id='body', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='partner_ids',
                                        value=Name(id='partner_ids', ctx=Load()),
                                    ),
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
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
                    name='_message_sms',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='body', annotation=None, type_comment=None),
                            arg(arg='subtype_id', annotation=None, type_comment=None),
                            arg(arg='partner_ids', annotation=None, type_comment=None),
                            arg(arg='number_field', annotation=None, type_comment=None),
                            arg(arg='sms_numbers', annotation=None, type_comment=None),
                            arg(arg='sms_pid_to_number', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Main method to post a message on a record using SMS-based notification\n        method.\n\n        :param body: content of SMS;\n        :param subtype_id: mail.message.subtype used in mail.message associated\n          to the sms notification process;\n        :param partner_ids: if set is a record set of partners to notify;\n        :param number_field: if set is a name of field to use on current record\n          to compute a number to notify;\n        :param sms_numbers: see ``_notify_record_by_sms``;\n        :param sms_pid_to_number: see ``_notify_record_by_sms``;\n        ', kind=None),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='sms_pid_to_number', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='sms_pid_to_number', ctx=Load()),
                                    ops=[IsNot()],
                                    comparators=[Constant(value=None, kind=None)],
                                ),
                                body=Name(id='sms_pid_to_number', ctx=Load()),
                                orelse=Dict(keys=[], values=[]),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='number_field', ctx=Load()),
                                    BoolOp(
                                        op=And(),
                                        values=[
                                            Compare(
                                                left=Name(id='partner_ids', ctx=Load()),
                                                ops=[Is()],
                                                comparators=[Constant(value=False, kind=None)],
                                            ),
                                            Compare(
                                                left=Name(id='sms_numbers', ctx=Load()),
                                                ops=[Is()],
                                                comparators=[Constant(value=None, kind=None)],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='info', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='_sms_get_recipients_info',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[
                                                keyword(
                                                    arg='force_field',
                                                    value=Name(id='number_field', ctx=Load()),
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
                                Assign(
                                    targets=[Name(id='info_partner_ids', ctx=Store())],
                                    value=IfExp(
                                        test=Subscript(
                                            value=Name(id='info', ctx=Load()),
                                            slice=Constant(value='partner', kind=None),
                                            ctx=Load(),
                                        ),
                                        body=Attribute(
                                            value=Subscript(
                                                value=Name(id='info', ctx=Load()),
                                                slice=Constant(value='partner', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='ids',
                                            ctx=Load(),
                                        ),
                                        orelse=Constant(value=False, kind=None),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='info_number', ctx=Store())],
                                    value=IfExp(
                                        test=Subscript(
                                            value=Name(id='info', ctx=Load()),
                                            slice=Constant(value='sanitized', kind=None),
                                            ctx=Load(),
                                        ),
                                        body=Subscript(
                                            value=Name(id='info', ctx=Load()),
                                            slice=Constant(value='sanitized', kind=None),
                                            ctx=Load(),
                                        ),
                                        orelse=Subscript(
                                            value=Name(id='info', ctx=Load()),
                                            slice=Constant(value='number', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='info_partner_ids', ctx=Load()),
                                            Name(id='info_number', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='sms_pid_to_number', ctx=Load()),
                                                    slice=Subscript(
                                                        value=Name(id='info_partner_ids', ctx=Load()),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Name(id='info_number', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Name(id='info_partner_ids', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='partner_ids', ctx=Store())],
                                            value=BinOp(
                                                left=Name(id='info_partner_ids', ctx=Load()),
                                                op=Add(),
                                                right=BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Name(id='partner_ids', ctx=Load()),
                                                        List(elts=[], ctx=Load()),
                                                    ],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Name(id='info_partner_ids', ctx=Load()),
                                    ),
                                    body=[
                                        If(
                                            test=Name(id='info_number', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='sms_numbers', ctx=Store())],
                                                    value=BinOp(
                                                        left=List(
                                                            elts=[Name(id='info_number', ctx=Load())],
                                                            ctx=Load(),
                                                        ),
                                                        op=Add(),
                                                        right=BoolOp(
                                                            op=Or(),
                                                            values=[
                                                                Name(id='sms_numbers', ctx=Load()),
                                                                List(elts=[], ctx=Load()),
                                                            ],
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=UnaryOp(
                                                        op=Not(),
                                                        operand=Name(id='sms_numbers', ctx=Load()),
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='sms_numbers', ctx=Store())],
                                                            value=List(
                                                                elts=[Constant(value=False, kind=None)],
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[],
                                                ),
                                            ],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Name(id='subtype_id', ctx=Load()),
                                ops=[Is()],
                                comparators=[Constant(value=False, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='subtype_id', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.model.data', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_xmlid_to_res_id',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='mail.mt_note', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='message_post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='body',
                                        value=Call(
                                            func=Name(id='plaintext2html', ctx=Load()),
                                            args=[
                                                Call(
                                                    func=Name(id='html2plaintext', ctx=Load()),
                                                    args=[Name(id='body', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                    ),
                                    keyword(
                                        arg='partner_ids',
                                        value=BoolOp(
                                            op=Or(),
                                            values=[
                                                Name(id='partner_ids', ctx=Load()),
                                                List(elts=[], ctx=Load()),
                                            ],
                                        ),
                                    ),
                                    keyword(
                                        arg='message_type',
                                        value=Constant(value='sms', kind=None),
                                    ),
                                    keyword(
                                        arg='subtype_id',
                                        value=Name(id='subtype_id', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='sms_numbers',
                                        value=Name(id='sms_numbers', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='sms_pid_to_number',
                                        value=Name(id='sms_pid_to_number', ctx=Load()),
                                    ),
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
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
                    name='_notify_thread',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='message', annotation=None, type_comment=None),
                            arg(arg='msg_vals', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='recipients_data', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='MailThread', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_notify_thread',
                                    ctx=Load(),
                                ),
                                args=[Name(id='message', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='msg_vals',
                                        value=Name(id='msg_vals', ctx=Load()),
                                    ),
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_notify_record_by_sms',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='message', ctx=Load()),
                                    Name(id='recipients_data', ctx=Load()),
                                ],
                                keywords=[
                                    keyword(
                                        arg='msg_vals',
                                        value=Name(id='msg_vals', ctx=Load()),
                                    ),
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Return(
                            value=Name(id='recipients_data', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_notify_record_by_sms',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='message', annotation=None, type_comment=None),
                            arg(arg='recipients_data', annotation=None, type_comment=None),
                            arg(arg='msg_vals', annotation=None, type_comment=None),
                            arg(arg='sms_numbers', annotation=None, type_comment=None),
                            arg(arg='sms_pid_to_number', annotation=None, type_comment=None),
                            arg(arg='check_existing', annotation=None, type_comment=None),
                            arg(arg='put_in_queue', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[
                            Constant(value=False, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                            Constant(value=False, kind=None),
                            Constant(value=False, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Notification method: by SMS.\n\n        :param message: mail.message record to notify;\n        :param recipients_data: see ``_notify_thread``;\n        :param msg_vals: see ``_notify_thread``;\n\n        :param sms_numbers: additional numbers to notify in addition to partners\n          and classic recipients;\n        :param pid_to_number: force a number to notify for a given partner ID\n              instead of taking its mobile / phone number;\n        :param check_existing: check for existing notifications to update based on\n          mailed recipient, otherwise create new notifications;\n        :param put_in_queue: use cron to send queued SMS instead of sending them\n          directly;\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='sms_pid_to_number', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='sms_pid_to_number', ctx=Load()),
                                    ops=[IsNot()],
                                    comparators=[Constant(value=None, kind=None)],
                                ),
                                body=Name(id='sms_pid_to_number', ctx=Load()),
                                orelse=Dict(keys=[], values=[]),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sms_numbers', ctx=Store())],
                            value=IfExp(
                                test=Compare(
                                    left=Name(id='sms_numbers', ctx=Load()),
                                    ops=[IsNot()],
                                    comparators=[Constant(value=None, kind=None)],
                                ),
                                body=Name(id='sms_numbers', ctx=Load()),
                                orelse=List(elts=[], ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sms_create_vals', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sms_all', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='sms.sms', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='body', ctx=Store())],
                            value=IfExp(
                                test=BoolOp(
                                    op=And(),
                                    values=[
                                        Name(id='msg_vals', ctx=Load()),
                                        Call(
                                            func=Attribute(
                                                value=Name(id='msg_vals', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='body', kind=None)],
                                            keywords=[],
                                        ),
                                    ],
                                ),
                                body=Subscript(
                                    value=Name(id='msg_vals', ctx=Load()),
                                    slice=Constant(value='body', kind=None),
                                    ctx=Load(),
                                ),
                                orelse=Attribute(
                                    value=Name(id='message', ctx=Load()),
                                    attr='body',
                                    ctx=Load(),
                                ),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sms_base_vals', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value='body', kind=None),
                                    Constant(value='mail_message_id', kind=None),
                                    Constant(value='state', kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='html2plaintext', ctx=Load()),
                                        args=[Name(id='body', ctx=Load())],
                                        keywords=[],
                                    ),
                                    Attribute(
                                        value=Name(id='message', ctx=Load()),
                                        attr='id',
                                        ctx=Load(),
                                    ),
                                    Constant(value='outgoing', kind=None),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partners_data', ctx=Store())],
                            value=ListComp(
                                elt=Name(id='r', ctx=Load()),
                                generators=[
                                    comprehension(
                                        target=Name(id='r', ctx=Store()),
                                        iter=Name(id='recipients_data', ctx=Load()),
                                        ifs=[
                                            Compare(
                                                left=Subscript(
                                                    value=Name(id='r', ctx=Load()),
                                                    slice=Constant(value='notif', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ops=[Eq()],
                                                comparators=[Constant(value='sms', kind=None)],
                                            ),
                                        ],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='partner_ids', ctx=Store())],
                            value=ListComp(
                                elt=Subscript(
                                    value=Name(id='r', ctx=Load()),
                                    slice=Constant(value='id', kind=None),
                                    ctx=Load(),
                                ),
                                generators=[
                                    comprehension(
                                        target=Name(id='r', ctx=Store()),
                                        iter=Name(id='partners_data', ctx=Load()),
                                        ifs=[],
                                        is_async=0,
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='partner_ids', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='partner', ctx=Store()),
                                    iter=Call(
                                        func=Attribute(
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
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='browse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='partner_ids', ctx=Load())],
                                        keywords=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='number', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='sms_pid_to_number', ctx=Load()),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Attribute(
                                                                value=Name(id='partner', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='mobile',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='partner', ctx=Load()),
                                                        attr='phone',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='sanitize_res', ctx=Store())],
                                            value=Subscript(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='phone_validation', ctx=Load()),
                                                        attr='phone_sanitize_numbers_w_record',
                                                        ctx=Load(),
                                                    ),
                                                    args=[
                                                        List(
                                                            elts=[Name(id='number', ctx=Load())],
                                                            ctx=Load(),
                                                        ),
                                                        Name(id='partner', ctx=Load()),
                                                    ],
                                                    keywords=[],
                                                ),
                                                slice=Name(id='number', ctx=Load()),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='number', ctx=Store())],
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Subscript(
                                                        value=Name(id='sanitize_res', ctx=Load()),
                                                        slice=Constant(value='sanitized', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Name(id='number', ctx=Load()),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='sms_create_vals', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Name(id='dict', ctx=Load()),
                                                        args=[Name(id='sms_base_vals', ctx=Load())],
                                                        keywords=[
                                                            keyword(
                                                                arg='partner_id',
                                                                value=Attribute(
                                                                    value=Name(id='partner', ctx=Load()),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            keyword(
                                                                arg='number',
                                                                value=Name(id='number', ctx=Load()),
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
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Name(id='sms_numbers', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='sanitized', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='phone_validation', ctx=Load()),
                                            attr='phone_sanitize_numbers_w_record',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='sms_numbers', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='tocreate_numbers', ctx=Store())],
                                    value=ListComp(
                                        elt=BoolOp(
                                            op=Or(),
                                            values=[
                                                Subscript(
                                                    value=Name(id='value', ctx=Load()),
                                                    slice=Constant(value='sanitized', kind=None),
                                                    ctx=Load(),
                                                ),
                                                Name(id='original', ctx=Load()),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Tuple(
                                                    elts=[
                                                        Name(id='original', ctx=Store()),
                                                        Name(id='value', ctx=Store()),
                                                    ],
                                                    ctx=Store(),
                                                ),
                                                iter=Call(
                                                    func=Attribute(
                                                        value=Name(id='sanitized', ctx=Load()),
                                                        attr='items',
                                                        ctx=Load(),
                                                    ),
                                                    args=[],
                                                    keywords=[],
                                                ),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                AugAssign(
                                    target=Name(id='sms_create_vals', ctx=Store()),
                                    op=Add(),
                                    value=ListComp(
                                        elt=Call(
                                            func=Name(id='dict', ctx=Load()),
                                            args=[Name(id='sms_base_vals', ctx=Load())],
                                            keywords=[
                                                keyword(
                                                    arg='partner_id',
                                                    value=Constant(value=False, kind=None),
                                                ),
                                                keyword(
                                                    arg='number',
                                                    value=Name(id='n', ctx=Load()),
                                                ),
                                                keyword(
                                                    arg='state',
                                                    value=IfExp(
                                                        test=Name(id='n', ctx=Load()),
                                                        body=Constant(value='outgoing', kind=None),
                                                        orelse=Constant(value='error', kind=None),
                                                    ),
                                                ),
                                                keyword(
                                                    arg='failure_type',
                                                    value=IfExp(
                                                        test=Name(id='n', ctx=Load()),
                                                        body=Constant(value='', kind=None),
                                                        orelse=Constant(value='sms_number_missing', kind=None),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='n', ctx=Store()),
                                                iter=Name(id='tocreate_numbers', ctx=Load()),
                                                ifs=[],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='existing_pids', ctx=Store()),
                                        Name(id='existing_numbers', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    List(elts=[], ctx=Load()),
                                    List(elts=[], ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Name(id='sms_create_vals', ctx=Load()),
                            body=[
                                AugAssign(
                                    target=Name(id='sms_all', ctx=Store()),
                                    op=BitOr(),
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
                                                        slice=Constant(value='sms.sms', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='sudo',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='sms_create_vals', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                                If(
                                    test=Name(id='check_existing', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='existing', ctx=Store())],
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
                                                                slice=Constant(value='mail.notification', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='search',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    List(
                                                        elts=[
                                                            Constant(value='|', kind=None),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='res_partner_id', kind=None),
                                                                    Constant(value='in', kind=None),
                                                                    Name(id='partner_ids', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Constant(value='&', kind=None),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='res_partner_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value=False, kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='sms_number', kind=None),
                                                                    Constant(value='in', kind=None),
                                                                    Name(id='sms_numbers', ctx=Load()),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='notification_type', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Constant(value='sms', kind=None),
                                                                ],
                                                                ctx=Load(),
                                                            ),
                                                            Tuple(
                                                                elts=[
                                                                    Constant(value='mail_message_id', kind=None),
                                                                    Constant(value='=', kind=None),
                                                                    Attribute(
                                                                        value=Name(id='message', ctx=Load()),
                                                                        attr='id',
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
                                            type_comment=None,
                                        ),
                                        For(
                                            target=Name(id='n', ctx=Store()),
                                            iter=Name(id='existing', ctx=Load()),
                                            body=[
                                                If(
                                                    test=BoolOp(
                                                        op=And(),
                                                        values=[
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='n', ctx=Load()),
                                                                        attr='res_partner_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='id',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[In()],
                                                                comparators=[Name(id='partner_ids', ctx=Load())],
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='n', ctx=Load()),
                                                                    attr='mail_message_id',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Name(id='message', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='existing_pids', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Attribute(
                                                                            value=Name(id='n', ctx=Load()),
                                                                            attr='res_partner_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        attr='id',
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
                                                            UnaryOp(
                                                                op=Not(),
                                                                operand=Attribute(
                                                                    value=Name(id='n', ctx=Load()),
                                                                    attr='res_partner_id',
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='n', ctx=Load()),
                                                                    attr='sms_number',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[In()],
                                                                comparators=[Name(id='sms_numbers', ctx=Load())],
                                                            ),
                                                            Compare(
                                                                left=Attribute(
                                                                    value=Name(id='n', ctx=Load()),
                                                                    attr='mail_message_id',
                                                                    ctx=Load(),
                                                                ),
                                                                ops=[Eq()],
                                                                comparators=[Name(id='message', ctx=Load())],
                                                            ),
                                                        ],
                                                    ),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='existing_numbers', ctx=Load()),
                                                                    attr='append',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Attribute(
                                                                        value=Name(id='n', ctx=Load()),
                                                                        attr='sms_number',
                                                                        ctx=Load(),
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
                                ),
                                Assign(
                                    targets=[Name(id='notif_create_values', ctx=Store())],
                                    value=ListComp(
                                        elt=Dict(
                                            keys=[
                                                Constant(value='mail_message_id', kind=None),
                                                Constant(value='res_partner_id', kind=None),
                                                Constant(value='sms_number', kind=None),
                                                Constant(value='notification_type', kind=None),
                                                Constant(value='sms_id', kind=None),
                                                Constant(value='is_read', kind=None),
                                                Constant(value='notification_status', kind=None),
                                                Constant(value='failure_type', kind=None),
                                            ],
                                            values=[
                                                Attribute(
                                                    value=Name(id='message', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Attribute(
                                                        value=Name(id='sms', ctx=Load()),
                                                        attr='partner_id',
                                                        ctx=Load(),
                                                    ),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Attribute(
                                                    value=Name(id='sms', ctx=Load()),
                                                    attr='number',
                                                    ctx=Load(),
                                                ),
                                                Constant(value='sms', kind=None),
                                                Attribute(
                                                    value=Name(id='sms', ctx=Load()),
                                                    attr='id',
                                                    ctx=Load(),
                                                ),
                                                Constant(value=True, kind=None),
                                                IfExp(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='sms', ctx=Load()),
                                                            attr='state',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='outgoing', kind=None)],
                                                    ),
                                                    body=Constant(value='ready', kind=None),
                                                    orelse=Constant(value='exception', kind=None),
                                                ),
                                                IfExp(
                                                    test=Compare(
                                                        left=Attribute(
                                                            value=Name(id='sms', ctx=Load()),
                                                            attr='state',
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='outgoing', kind=None)],
                                                    ),
                                                    body=Constant(value='', kind=None),
                                                    orelse=Attribute(
                                                        value=Name(id='sms', ctx=Load()),
                                                        attr='failure_type',
                                                        ctx=Load(),
                                                    ),
                                                ),
                                            ],
                                        ),
                                        generators=[
                                            comprehension(
                                                target=Name(id='sms', ctx=Store()),
                                                iter=Name(id='sms_all', ctx=Load()),
                                                ifs=[
                                                    BoolOp(
                                                        op=Or(),
                                                        values=[
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    Attribute(
                                                                        value=Name(id='sms', ctx=Load()),
                                                                        attr='partner_id',
                                                                        ctx=Load(),
                                                                    ),
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Attribute(
                                                                                value=Name(id='sms', ctx=Load()),
                                                                                attr='partner_id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='id',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[NotIn()],
                                                                        comparators=[Name(id='existing_pids', ctx=Load())],
                                                                    ),
                                                                ],
                                                            ),
                                                            BoolOp(
                                                                op=And(),
                                                                values=[
                                                                    UnaryOp(
                                                                        op=Not(),
                                                                        operand=Attribute(
                                                                            value=Name(id='sms', ctx=Load()),
                                                                            attr='partner_id',
                                                                            ctx=Load(),
                                                                        ),
                                                                    ),
                                                                    Compare(
                                                                        left=Attribute(
                                                                            value=Name(id='sms', ctx=Load()),
                                                                            attr='number',
                                                                            ctx=Load(),
                                                                        ),
                                                                        ops=[NotIn()],
                                                                        comparators=[Name(id='existing_numbers', ctx=Load())],
                                                                    ),
                                                                ],
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='notif_create_values', ctx=Load()),
                                    body=[
                                        Expr(
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
                                                                slice=Constant(value='mail.notification', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='sudo',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    attr='create',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='notif_create_values', ctx=Load())],
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
                                            Name(id='existing_pids', ctx=Load()),
                                            Name(id='existing_numbers', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        For(
                                            target=Name(id='sms', ctx=Store()),
                                            iter=Name(id='sms_all', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='notif', ctx=Store())],
                                                    value=Call(
                                                        func=Name(id='next', ctx=Load()),
                                                        args=[
                                                            GeneratorExp(
                                                                elt=Name(id='n', ctx=Load()),
                                                                generators=[
                                                                    comprehension(
                                                                        target=Name(id='n', ctx=Store()),
                                                                        iter=Name(id='existing', ctx=Load()),
                                                                        ifs=[
                                                                            BoolOp(
                                                                                op=Or(),
                                                                                values=[
                                                                                    BoolOp(
                                                                                        op=And(),
                                                                                        values=[
                                                                                            Compare(
                                                                                                left=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='n', ctx=Load()),
                                                                                                        attr='res_partner_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[In()],
                                                                                                comparators=[Name(id='existing_pids', ctx=Load())],
                                                                                            ),
                                                                                            Compare(
                                                                                                left=Attribute(
                                                                                                    value=Attribute(
                                                                                                        value=Name(id='n', ctx=Load()),
                                                                                                        attr='res_partner_id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                    attr='id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[
                                                                                                    Attribute(
                                                                                                        value=Attribute(
                                                                                                            value=Name(id='sms', ctx=Load()),
                                                                                                            attr='partner_id',
                                                                                                            ctx=Load(),
                                                                                                        ),
                                                                                                        attr='id',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                    BoolOp(
                                                                                        op=And(),
                                                                                        values=[
                                                                                            UnaryOp(
                                                                                                op=Not(),
                                                                                                operand=Attribute(
                                                                                                    value=Name(id='n', ctx=Load()),
                                                                                                    attr='res_partner_id',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                            ),
                                                                                            Compare(
                                                                                                left=Attribute(
                                                                                                    value=Name(id='n', ctx=Load()),
                                                                                                    attr='sms_number',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[In()],
                                                                                                comparators=[Name(id='existing_numbers', ctx=Load())],
                                                                                            ),
                                                                                            Compare(
                                                                                                left=Attribute(
                                                                                                    value=Name(id='n', ctx=Load()),
                                                                                                    attr='sms_number',
                                                                                                    ctx=Load(),
                                                                                                ),
                                                                                                ops=[Eq()],
                                                                                                comparators=[
                                                                                                    Attribute(
                                                                                                        value=Name(id='sms', ctx=Load()),
                                                                                                        attr='number',
                                                                                                        ctx=Load(),
                                                                                                    ),
                                                                                                ],
                                                                                            ),
                                                                                        ],
                                                                                    ),
                                                                                ],
                                                                            ),
                                                                        ],
                                                                        is_async=0,
                                                                    ),
                                                                ],
                                                            ),
                                                            Constant(value=False, kind=None),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='notif', ctx=Load()),
                                                    body=[
                                                        Expr(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='notif', ctx=Load()),
                                                                    attr='write',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Dict(
                                                                        keys=[
                                                                            Constant(value='notification_type', kind=None),
                                                                            Constant(value='notification_status', kind=None),
                                                                            Constant(value='sms_id', kind=None),
                                                                            Constant(value='sms_number', kind=None),
                                                                        ],
                                                                        values=[
                                                                            Constant(value='sms', kind=None),
                                                                            Constant(value='ready', kind=None),
                                                                            Attribute(
                                                                                value=Name(id='sms', ctx=Load()),
                                                                                attr='id',
                                                                                ctx=Load(),
                                                                            ),
                                                                            Attribute(
                                                                                value=Name(id='sms', ctx=Load()),
                                                                                attr='number',
                                                                                ctx=Load(),
                                                                            ),
                                                                        ],
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
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='sms_all', ctx=Load()),
                                    UnaryOp(
                                        op=Not(),
                                        operand=Name(id='put_in_queue', ctx=Load()),
                                    ),
                                ],
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='sms_all', ctx=Load()),
                                                    attr='filtered',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Lambda(
                                                        args=arguments(
                                                            posonlyargs=[],
                                                            args=[arg(arg='sms', annotation=None, type_comment=None)],
                                                            vararg=None,
                                                            kwonlyargs=[],
                                                            kw_defaults=[],
                                                            kwarg=None,
                                                            defaults=[],
                                                        ),
                                                        body=Compare(
                                                            left=Attribute(
                                                                value=Name(id='sms', ctx=Load()),
                                                                attr='state',
                                                                ctx=Load(),
                                                            ),
                                                            ops=[Eq()],
                                                            comparators=[Constant(value='outgoing', kind=None)],
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            attr='send',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='auto_commit',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='raise_exception',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Constant(value=True, kind=None),
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
